import json
from google.analytics.data import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest

def get_ga_stats():
    # 用下载的 JSON 凭据初始化客户端
    client = BetaAnalyticsDataClient.from_service_account_json('act-geneticflow-cb371a4de859.json')
    
    # 替换为你的 GA4 property ID（形如：XXXXXXXX）
    property_id = '404457588'
    
    # 构建请求，注意这里定义的 metric 名称要与 GA4 的命名一致
    request = RunReportRequest(
        property=f"properties/{property_id}",
        metrics=[
            {"name": "activeUsers"},
            {"name": "newUsers"},
            {"name": "eventCount"}
        ],
        # 定义数据统计的日期范围，可根据需求调整
        date_ranges=[{"start_date": "2023-08-27", "end_date": "today"}],
    )
    
    response = client.run_report(request)
    
    # 处理返回数据，示例中按日期返回每天的统计数据
    stats = {}
    for row in response.rows:
    #    date = row.dimension_values[0].value if row.dimension_values else "总计"
        stats['activeUsers'] = row.metric_values[0].value
        stats['newUsers'] = row.metric_values[1].value
        stats['eventCount'] = row.metric_values[2].value
    
    return stats
 
 
if __name__ == "__main__":
    result = get_ga_stats()
    with open("google_analytics.json", "w", encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False)
    # print(get_ga_stats())
