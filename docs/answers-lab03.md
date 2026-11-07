# Lab 03 – Câu trả lời thảo luận

## 1. Merge base là gì?

Merge base là commit tổ tiên chung gần nhất của hai nhánh, tức điểm mà hai nhánh bắt đầu tách ra khỏi nhau. Có thể xem bằng lệnh `git merge-base <nhánh A> <nhánh B>`.

Khi merge, Git thực hiện so sánh ba bên (three-way merge) giữa merge base, đầu nhánh A và đầu nhánh B:
- Nếu chỉ một nhánh thay đổi một đoạn so với merge base, Git tự lấy thay đổi đó.
- Nếu cả hai nhánh cùng sửa một đoạn theo hai cách khác nhau, Git không biết chọn bên nào nên báo conflict.

Trong bài này, `feature/vietnamese-messages` và `feature/show-added-title` cùng tách ra từ một commit trên `master` và cùng sửa dòng `print(...)` trong `Cart.add_dvd()`. Sau khi PR của nhánh thứ nhất được merge, `master` đã có thay đổi mới, còn nhánh thứ hai vẫn so với merge base cũ nên Git báo conflict. Ngoài ra, ở Phần B, PR bugfix chọn base là `feature/discount` thì merge base cũng là nhánh tính năng, nên PR chỉ hiện đúng các commit sửa lỗi.

## 2. Vì sao master và release/* phải dùng revert?

`master` và `release/*` là lịch sử đã chia sẻ: nhiều người đã pull, nhánh khác đã tách ra từ đó, và `release/*` còn là baseline đã phát hành.

- `git reset` dời con trỏ nhánh về commit cũ và viết lại lịch sử. Nếu phải push lên nhánh đã chia sẻ thì phải `--force`. Khi đó lịch sử của người khác bị lệch so với remote, dễ gây conflict, mất commit và phá vỡ tính toàn vẹn của baseline.
- `git revert` không sửa lịch sử cũ. Nó tạo thêm một commit mới đảo ngược thay đổi, nên lịch sử chỉ đi tiếp về phía trước, push bình thường không cần force.
- Revert còn giữ được dấu vết: ai đã thay đổi, khi nào, vì sao bị hoàn tác. Điều này phù hợp với mục tiêu kiểm soát thay đổi và truy vết của quản lý cấu hình phần mềm.
- Ngoài ra `master` và `release/*` có branch protection, mọi thay đổi bắt buộc đi qua Pull Request. Revert đi qua nhánh riêng và PR (ví dụ `bugfix/revert-show-added-title`) nên vẫn được review.

Với merge commit như PR của `feature/show-added-title`, phải dùng `git revert -m 1 <sha>` để chỉ rõ giữ lại nhánh cha thứ nhất (`master`) và đảo ngược các thay đổi đến từ nhánh còn lại.

Tóm lại: `reset` chỉ an toàn với commit chưa push (như nhánh nháp `topic/undo-practice`), còn commit đã chia sẻ thì dùng `revert`.