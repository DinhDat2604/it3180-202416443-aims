# Lab 04 – Trả lời câu hỏi thảo luận

## 1. Vì sao release/* không merge vào master? So sánh với GitFlow

Trong Lab này, `release/lab04` chỉ là bản đóng băng của v1.0.0, dùng để bảo trì sau này. Master thì vẫn phát triển tiếp, ví dụ đã có thêm `sort_by_cost` mà release/lab04 không có. Lúc tạo release, mọi commit của nó đều đã nằm sẵn trên master (lệnh `git log master..release/lab04` ra rỗng), nên không có gì cần merge về. Nếu sau này có hotfix trên release thì đưa sang master bằng cherry-pick (Lab 05), như vậy master không bị kéo theo những thay đổi khác của nhánh release.

Trong GitFlow thì khác: nhánh release được tách ra từ develop, sau khi ổn định thì merge ngược về cả master và develop, và master chỉ chứa các bản đã phát hành. Cách của lab này gọn hơn: chỉ có master làm nhánh chính, release/* là các nhánh bảo trì riêng biệt, không phải merge hai chiều.

## 2. Vì sao lên 1.0.0 mà không phải 0.4.0?

Theo Semantic Versioning, `0.y.z` là giai đoạn đầu, chưa ổn định, nên các Lab 01–03 mới đặt là v0.1.0 đến v0.3.0. Đến Lab 04 chương trình đã có đủ chức năng chính (giỏ hàng, tìm kiếm, giảm giá), có test và đã sửa lỗi nên được phát hành chính thức lần đầu. Vì vậy lên 1.0.0 để báo đây là bản ổn định đầu tiên, và từ đó các bản sau mới tăng theo quy tắc MAJOR.MINOR.PATCH (sửa lỗi lên 1.0.1, thêm tính năng lên 1.1.0). Nếu chỉ lên 0.4.0 thì vẫn là bản chưa ổn định.
