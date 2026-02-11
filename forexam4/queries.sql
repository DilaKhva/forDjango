-- A VARIANT
-- Chiqarilgan yili bo'yicha kitoblarni tartiblash
SELECT
    id,
    title,
    published_year,
    author_id,
    genre_id
FROM books
ORDER BY published_year DESC;

-- Har bir janr bo'yicha nechta kitob borligini chiqaring
SELECT
    g.name AS genre_name,
    COUNT(b.id) AS books_count
FROM genres g
LEFT JOIN books b ON g.id = b.genre_id
GROUP BY g.id, g.name
ORDER BY books_count DESC;

-- Comment yozilmagan kitoblarni chiqaring
SELECT
    b.id,
    b.title,
    b.published_year,
    a.full_name AS author_name
FROM books b
LEFT JOIN comments c ON b.id = c.book_id
LEFT JOIN authors a ON b.author_id = a.id
WHERE c.id IS NULL
ORDER BY b.title;

-- Eng ko'p komment yozilgan 5 ta kitobni chiqaring
SELECT
    b.id,
    b.title,
    a.full_name AS author_name,
    COUNT(c.id) AS comments_count
FROM books b
INNER JOIN comments c ON b.id = c.book_id
INNER JOIN authors a ON b.author_id = a.id
GROUP BY b.id, b.title, a.full_name
ORDER BY comments_count DESC
LIMIT 5;

-- B VARIANT
-- Har bir country bo'yicha nechta muallif borligini chiqaring
SELECT
    country,
    COUNT(id) AS authors_count
FROM authors
GROUP BY country
ORDER BY authors_count DESC;

-- Kitob yozmagan mualliflarni chiqaring
SELECT
    a.id,
    a.full_name,
    a.country
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
WHERE b.id IS NULL
ORDER BY a.full_name;

-- Har bir foydalanuvchi nechta komment yozganini chiqaring
SELECT
    u.id,
    u.full_name,
    u.email,
    COUNT(c.id) AS comments_count
FROM users u
LEFT JOIN comments c ON u.id = c.user_id
GROUP BY u.id, u.full_name, u.email
ORDER BY comments_count DESC;

-- Har bir muallif yozgan kitoblar sonini chiqaring
SELECT
    a.id,
    a.full_name,
    a.country,
    COUNT(b.id) AS books_count
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
GROUP BY a.id, a.full_name, a.country
ORDER BY books_count DESC;

