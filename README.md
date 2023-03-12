<p align="center">
   <a href="https://www.uit.edu.vn/">
      <img src="https://i.imgur.com/WmMnSRt.png" border="none">
   </a>
</p>
<h1 align="center">
    CS114.N11.KHCL - Máy học
</h1>

<h2>
   Giới thiệu môn học   
</h2>

- *Tên môn học:* Máy học
- *Mã môn học:* CS114
- *Mã lớp:*  CS114.N11.KHCL
- *Năm học:* HK1 (2022-2023)
- *Giảng viên:* Ths. Phạm Nguyễn Trường An - truonganpn@uit.edu.vn

<h2>
   Giới thiệu nhóm
</h2>

- *Thông tin thành viên:* 

<table align="center">
      <tr>
       <th>Họ và Tên</th>
       <th>MSSV</th>
       <th>Github</th>
       <th>Email</th>
      </tr>
      <tr>
       <td>Trần Quang Nhật</td>
       <td>20520675</td>
       <td>https://github.com/Yamakaze-chan</td>
       <td>20520675@gm.uit.edu.vn</td>  
      </tr>
      <tr>
       <td>Võ Thành Thái</td>
       <td>20520305</td>
       <td>https://github.com/thaivo02</td>
       <td>20520305@gm.uit.edu.vn</td>  
      </tr>
</table>

<h2>
  Chủ đề báo cáo 
</h2>

- *Tên chủ đề:* xác định và nhận diện biển số xe

<h3>Mô tả đồ án: </h3>

<b>Ngữ cảnh ứng dụng</b>

<p>Ngày nay, dưới sự phát triển của xã hội, chất lượng cuộc sống càng được nâng cao thì số
lượng phương tiện tham gia giao thông ngày càng nhiều. Điều này đặt ra một thách thức lớn với
các cơ quan quản lý trật tự giao thông và đô thị. Bên cạnh những người dân tham gia giao thông
có ý thức tốt, có văn hóa thì vẫn còn một bộ phận không nhỏ những người tham gia giao thông
có ý thức kém. Do đó, nếu áp dụng các mô hình hình máy học thì có thể hỗ trợ giảm áp lực và
tăng hiệu suất của các cơ quan quản lý trật tự giao thông và đô thị.</p>
<p>Nhằm nâng cao ý thức tham gia giao thông của người dân, Nhà nước đã có các chế tài
xử lý phù hợp. Thế nhưng để xử lý “đúng người, đúng tội” thì vẫn còn là một bài toán khó với
cảnh sát giao thông. Vì thế, chúng tôi đề xuất áp dụng máy học trong việc nhận diện biển số
phương tiện giao thông đường bộ, từ đó có thể dễ dàng giám sát cũng như xử lý các trường hợp
vi phạm giao thông.</p>
<p>Dữ liệu từ các camera giám sát đường phố có thể được sử dụng để xác định biển số
phương tiện vi phạm một cách nhanh và chuẩn xác nhất, tạo tiền đề cho việc xử lý vi phạm giao
thông tự động mà không cần sự can thiệp của con người. Vì thế nhóm đề xuất sử dụng mô hình
YOLO nhằm nhận diện, phân loại và đọc biển số xe.</p>

<b><i>Input</i></b>
- 1 tấm ảnh hoặc một đoạn video đường phố ở một đoạn đường.

<b><i>Output</i></b>
- Loại biển số xe và các ký tự đọc được trên các biển số.

<h3>Mô tả dữ liệu: </h3>
<p>Dữ liệu cho bài toán được thu thập từ các camera ở Đà Nẵng thông qua trang web. Nhóm đã lấy các khung hình trong video ghi hình từ trang web <a href="https://camera.0511.vn/camera.html">Camera Đà Nẵng</a>, sau đó gắn
nhãn biển số xe cho từng khung hình, sử dụng một số ảnh biển số phương tiện để gắn nhãn các
kí tự trong biển số phương tiện, để tạo thành 2 bộ dataset.</p>

<b>Số lượng, độ đa dạng của bộ dữ liệu</b>

- Dataset dành cho nhận diện biển số phương tiện: (Tổng cộng 4264 ảnh).
- Dataset dành cho nhận diện ký tự trên biển số phương tiện: (Tổng cộng 2446 ảnh).
- Phân chia tập dữ liệu: 
   - Train/Valid/Test : 88% / 4% / 8%.
- Tiền xử lý dữ liệu: đưa ảnh về kích thước 640 x 640

<h3>Phương pháp</h3>
<p> Sử dụng model YOLO v8 </p>
