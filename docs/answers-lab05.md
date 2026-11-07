# Lab 05 – Trả lời câu hỏi thảo luận

## 1. Ưu, nhược điểm của upstream first so với release first

Upstream first là sửa trên master trước rồi cherry-pick sang các nhánh release. Ưu điểm là bản sửa luôn có trên master nên các bản sau không bị lỗi cũ quay lại. Nhược điểm là phải chờ sửa và review trên master, trong khi master có thể đã có nhiều thay đổi khác, nên chậm hơn khi cần vá gấp.

Release first, như trong học phần này, là tạo hotfix từ nhánh release đang lỗi. Ưu điểm là sửa nhanh và đúng trên bản đang chạy, không bị lẫn tính năng mới của master. Nhược điểm là dễ quên đưa bản sửa về master và các release khác, nên phải kiểm toán lại bằng Phần F.

## 2. Nếu quên lan truyền bản sửa sang release/lab05 thì lệnh nào phát hiện?

Lệnh `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"` sẽ chỉ ra 1 commit thay vì 2. Vòng lặp kiểm tra ở Phần F cũng in `0` cho v1.1.0 thay vì `1`, vì tìm "lion" vẫn không ra. Ngoài ra `git cherry -v origin/release/lab05 origin/master` sẽ hiện dấu `+` ở commit sửa lỗi, nghĩa là release/lab05 chưa có bản tương đương.