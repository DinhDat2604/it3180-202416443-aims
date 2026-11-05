# Lab 01 – Câu trả lời thảo luận

## 1. Vì sao dùng `git mv`?

`git mv` vừa di chuyển tệp vừa đưa việc đổi tên vào vùng staging trong một
lệnh. Về bản chất Git không lưu "đổi tên" mà so sánh nội dung giữa các
commit; khi nội dung giống nhau gần 100% (ở đây là 100%) Git nhận ra đó là
một tệp được đổi tên (rename) chứ không phải xóa tệp cũ và thêm tệp mới.
Nhờ vậy lịch sử của `cart.py` và `dvd.py` được giữ nguyên: lệnh
`git log --oneline --follow -- aims/cart.py` vẫn hiện được commit
`feat: add initial DVD, Cart and demo program` từ trước khi di chuyển, và
tab Files changed của PR hiển thị `renamed`. Nếu tự xóa và tạo lại tệp thì
diff sẽ rất lớn, khó review và dễ mất khả năng truy vết.

## 2. `release/lab01` có phải baseline không?

Có. Baseline là phiên bản đã được thống nhất và về sau chỉ được thay đổi qua
quy trình kiểm soát. `release/lab01` được tạo từ `master` sau khi toàn bộ
thay đổi (refactor, câu trả lời thảo luận) đã được đưa vào `master` qua Pull
Request, nên nó đại diện cho một trạng thái hoàn chỉnh của bài Lab 01, và
đây chính là bản nộp. Nhánh này được đóng băng: không commit trực tiếp lên
đó, nếu cần sửa thì phải đi qua một nhánh hotfix và Pull Request (Lab 05).
Ở Lab 04, nhánh sẽ được bảo vệ bằng rule và đánh dấu bằng tag để định danh
chính xác phiên bản.

## 3. Vì sao không commit thẳng `master` dù làm một mình?

Vì `master` là nguồn của mọi baseline và bản nộp, nên mọi thay đổi vào
đó phải được kiểm soát, kể cả khi chỉ có một người. Làm qua nhánh và Pull
Request giúp:
- Lưu vết rõ ràng: mỗi thay đổi có mục đích, mô tả, cách kiểm thử và gắn với
  một nhánh/PR, dễ truy vết và dễ hoàn tác bằng `revert`.
- Có điểm dừng để tự rà soát (xem Files changed) trước khi tích hợp, như ở
  Lab 01 em đã phát hiện sót commit sửa import nhờ kiểm tra lại lịch sử.
- Giữ `master` luôn ở trạng thái chạy được, thay vì để lỗi lọt thẳng vào
  nhánh chính.
- Tập đúng thói quen quy trình nhóm, để khi làm việc với nhiều người không
  phải đổi cách làm.