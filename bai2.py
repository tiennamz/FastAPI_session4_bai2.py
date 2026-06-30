from fastapi import FastAPI
app = FastAPI()
orders = [
    {"id": 1, "customer_name": "Nguyễn Văn An", "total": 250000, "status": "pending"},
    {"id": 2, "customer_name": "Trần Thị Bình", "total": 500000, "status": "paid"},
    {"id": 3, "customer_name": "Lê Văn Cường", "total": 150000, "status": "cancelled"},
    {"id": 4, "customer_name": "Phạm Thị Dung", "total": 320000, "status": "pending"}
]
@app.get("/orders/status/{status}")
def get_orders_by_status(status: str):
    if status not in ('pending', 'paid', 'cancelled'):
        return {
            'message': 'Trạng thái đơn hàng không hợp lệ'
        }
    list_orders = []
    list_orders.append([order for order in orders if order.get('status') == status])
    return list_orders

'''
- Endpoint hiện tại có Path Parameter không? Có
- Path Parameter trong bài này là gì? @app.get("/orders/status/{status}")
- Khi gọi /orders/status/pending, biến status nhận giá trị gì? pending
- Vì sao API hiện tại trả về sai dữ liệu? Vì ta k dùng đến ststus trong hàm
- Dòng code nào đang khiến API bỏ qua giá trị status? return orders
'''
