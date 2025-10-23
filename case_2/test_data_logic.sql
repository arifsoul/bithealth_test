-- Kueri ini menemukan 5 kunjungan terbaru ke departemen Neurologi
-- dengan kriteria spesifik pada usia pasien dan jumlah gejala.

SELECT
    p.name AS "patients.name",
    p.age AS "patients.age",
    v.visit_date AS "visits.visit_date",
    COUNT(s.id) AS symptom_count
FROM
    visits v
JOIN
    patients p ON v.patient_id = p.id
JOIN
    symptoms s ON v.id = s.visit_id
WHERE
    -- 1. Filter departemen
    v.department = 'Neurology'
    -- 2. Filter usia pasien
    AND p.age > 50
GROUP BY
    v.id, -- Group by visit untuk menghitung gejala per kunjungan
    p.name,
    p.age,
    v.visit_date
HAVING
    -- 3. Filter jumlah gejala (setelah grouping)
    COUNT(s.id) >= 3
ORDER BY
    -- 4. Urutkan berdasarkan kunjungan terbaru
    v.visit_date DESC
LIMIT 5; -- 5. Ambil 5 teratas
