# البرمجة التفرعية – موقع المراجعة والاختبار

## نظرة عامة
موقع ويب تعليمي لمادة البرمجة التفرعية (النظري) يتيح المراجعة والاختبار الذاتي لـ 10 محاضرات.

## هيكل المشروع
```
index.html        - الموقع الكامل (HTML + CSS + JavaScript في ملف واحد)
ibrahim.html      - موقع آخر للمادة نفسها (موجود من قبل)
attached_assets/  - ملفات PDF الأصلية للمادة (10 محاضرات)
```

## التشغيل
```bash
python3 -m http.server 5000
```
ثم افتح: http://localhost:5000

## محتوى الموقع
- **10 محاضرات** كل منها يحتوي على:
  - **قسم المراجعة**: 8-10 أسئلة مع إجابات تفصيلية (اكشف/أخفِ)
  - **قسم الاختبار**: 10 أسئلة صح/خطأ + اختيار من متعدد مع تصحيح وشرح

## المحاضرات
1. مقدمة في البرمجة التفرعية (Flynn، الجدولة، Thread/Process)
2. أساسيات MPI (MPI_Send، MPI_Recv، Communicator)
3. العمليات الجماعية (Broadcast، Scatter، Gather، Reduce)
4. الإرسال غير المتزامن (MPI_Isend، MPI_Irecv، MPI_Wait)
5. دوال Wait/Test المتقدمة (Waitany، Waitall، Testsome)
6. قابلية التوازي (تحليل التبعية، ضرب المصفوفات)
7. مقاييس الأداء (Speedup، Efficiency، Amdahl، Gustafson)
8. مثال جمع الأرقام (Master/Slave، Partition vs Broadcast)
9. معالجة الصور (Bitmap، RGB، Shifting، Scaling، Rotation)
10. مجموعة Mandelbrot (Static vs Dynamic Task Assignment، Work Pool)

## تفضيلات المستخدم
- اللغة: عربي (RTL)
- التصميم: حديث نظيف
