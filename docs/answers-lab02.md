# Lab 02 – Câu trả lời thảo luận

## 1. Vì sao phải đồng bộ master trước khi gửi PR?

Nhánh `feature/search-by-title` được tạo từ `master` cũ, lúc đó `master`
chưa có `Cart.print_cart()`. Trong lúc đó PR `feature/cart-print` được
merge nên `master` đi trước nhánh của em. Nếu gửi PR ngay, em không biết
code mới của mình có chạy cùng với thay đổi mới trên `master` hay không,
và PR có thể báo xung đột hoặc làm hỏng `main.py` sau khi merge. Em đã chạy
`git merge origin/master` vào nhánh rồi chạy `python main.py` để kiểm tra
tích hợp ngay trên nhánh của mình, xử lý mọi vấn đề trước khi người khác
review. Nhờ vậy thứ được duyệt là thứ sẽ được tích hợp thật sự (đúng nguyên
tắc SCM "thứ được duyệt = thứ được tích hợp").

## 2. Khi nào không được rebase?

Không rebase khi các commit đã được chia sẻ, tức đã push và người khác có
thể đã dựa vào chúng (nhánh `master`, `release/*`, hoặc nhánh mà người
khác đang làm chung). Rebase viết lại lịch sử và tạo commit với mã băm mới,
nên người khác sẽ bị lệch lịch sử và phải xử lý lại. Quy tắc 5 của Release
Flow: chỉ viết lại lịch sử (amend, reset, rebase) trên commit chưa chia sẻ.
Với commit đã chia sẻ thì dùng merge hoặc `git revert`. Trong bài, rebase
chỉ được dùng ở bước "Rebase and merge" cho PR use case, khi commit chưa
ai khác dùng.

## 3. `feature/*` khác `topic/*` thế nào?

`feature/*` dùng cho **tính năng** của sản phẩm (ví dụ `feature/cart-print`,
`feature/search-by-title`: thêm chức năng người dùng thấy được). `topic/*`
dùng cho **chủ đề** khác không phải tính năng, như tài liệu hoặc cấu hình
(ví dụ `topic/pr-template`, `topic/use-case-diagram`). Cả hai đều tạo từ
`master` và merge vào `master` qua Pull Request; chỉ khác ở mục đích, giúp
nhìn tên nhánh là biết nhánh làm gì (quy tắc "một nhánh, một mục đích").