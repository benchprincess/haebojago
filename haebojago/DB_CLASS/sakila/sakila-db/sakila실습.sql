USE sakila;

-- 문제 1
-- SELECT f.title
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- WHERE a.first_name = 'JOHNNY' AND a.last_name = 'LOLLOBRIGIDA';

-- 문제 2. 각 카테고리 별로 몇개의 영화가 있는지 조회하시오.
-- SELECT c.name, COUNT(fc.film_id) AS number_of_film
-- FROM category c
-- JOIN film_category fc ON c.category_id = fc.category_id
-- GROUP BY c.name;

-- 문제 3. 고객 ID가 5인 고객의 모든 대여 기록을 조회하시오.
-- SELECT r.rental_date, f.title
-- FROM rental r
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE r.customer_id = 5;

-- 문제 4. 가장 최근에 데이터베이스에 추가된 10개의 영화 제목을 조회하시오.
-- SELECT title, release_year
-- FROM film
-- ORDER BY release_year DESC, title
-- LIMIT 10;

-- 문제 1 . 'ACADEMY DINOSAUR' 영화에 출연한 모든 배우의 이름을 조회하시오.
-- SELECT a.first_name, a.last_name
-- FROM actor a
-- JOIN film_actor fa ON a.actor_id = fa.actor_id
-- JOIN film f ON fa.film_id = fi.film_id
-- WHERE f.title = 'ACADEMY DINOSAUR';

-- 문제 2. 'ACADEMY DINOSAUR' 영화를 대여한 모든 고객의 이름을 조회하시오.
-- SELECT c.first_name, c.last_name
-- FROM customer c
-- JOIN rental r ON c.customer_id = r.customer_id
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE f.title = 'ACADEMY DINOSAUR';

-- SELECT c.customer_id, c.first_name, c.last_name, MAX(r.rental_date) as last_rental_date, f.title
-- FROM customer c
-- JOIN rental r ON c.customer_id = r.customer_id
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- GROUP BY c.customer_id, c.first_name, c.last_name, f.title;

-- SELECT f.title, COUNT(r.rental_id) AS rental_count
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- GROUP BY f.title
-- ORDER BY rental_count DESC
-- LIMIT 1;

-- SELECT c.name, AVG(f.rental_rate) as average_rental_rate
-- FROM category c
-- JOIN film_category fc ON c.category_id = fc.category_id
-- JOIN film f ON fc.film_id = f.film_id
-- GROUP BY c.name;

-- 문제 . 각 월별로 총 매출액을 계산하시오.
-- SELECT YEAR(p.payment_date) as year, MONTH(p.payment_date) as month, SUM(p.amount) as total_sales
-- FROM payment p
-- GROUP BY YEAR(p.payment_date), MONTH(p.payment_date);

-- 문제: 각 배우별로 출연한 영화 수를 계산하시오.
-- SELECT a.first_name, a.last_name, COUNT(fa.film_id) as number_of_films
-- FROM actor a
-- JOIN film_actor fa ON a.actor_id = fa.actor_id
-- GROUP BY a.first_name, a.last_name;

-- 서브쿼리 및 고급 기능
-- 가장 수익이 많은 영화 조회
-- 문제: 가장 많은 수익을 낸 영화의 제목과 수익을 조회하시오.
-- 힌트:
-- payment, rental, inventory, film 테이블을 조인합니다.
-- 각 영화별로 총 수익을 계산하고, 가장 높은 수익을 낸 영화를 찾습니다.
-- 정답:
-- SELECT f.title, SUM(p.amount) AS total_revenue
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- JOIN payment p ON r.rental_id = p.rental_id
-- GROUP BY f.title
-- ORDER BY total_revenue DESC
-- LIMIT 1;

-- 평균 대여 요금보다 높은 요금의 영화 조회
-- 문제: 평균 대여 요금보다 높은 요금의 영화 제목과 요금을 조회하시오.
-- 힌트:
-- film 테이블에서 평균 대여 요금(rental_rate)을 계산합니다.
-- 평균보다 높은 대여 요금을 가진 영화를 찾습니다.
-- 정답:
-- SELECT f.title, f.rental_rate
-- FROM film f
-- WHERE f.rental_rate > (SELECT AVG(rental_rate) FROM film);

-- 3. 가장 활동적인 고객 조회
-- 문제: 가장 많은 영화를 대여한 고객의 이름과 대여 횟수를 조회하시오.  
-- 힌트:   
-- `rental`과 `customer` 테이블을 조인합니다.
-- 각 고객별로 대여 횟수를 계산하고 가장 많이 대여한 고객을 찾습니다.
-- 정답
-- SELECT c.customer_id, c.first_name, c.last_name, COUNT(r.rental_id) AS rental_count
-- FROM rental r
-- JOIN customer c ON r.customer_id = c.customer_id
-- GROUP BY c.customer_id
-- ORDER BY rental_count DESC
-- LIMIT 1;

-- SELECT f.title, COUNT(r.rental_id) AS rental_count
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS'
-- GROUP BY f.title
-- GROUP BY rental_count DESC
-- LIMIT 1;

-- 새로운 영화 추가
-- 문제: 'film' 테이블에 'New Adventure Movie'라는 새로운 영화를 추가하시오.
-- 힌트:
-- INSERT INTO 구문을 사용하여 film 테이블에 새로운 레코드를 추가합니다.
-- 모든 필요한 필드에 대한 값을 명시합니다.
-- 정답:
-- INSERT INTO film (title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features)
-- VALUES ('New Adventure Movie', 'A thrilling adventure of the unknown'

-- 고객 정보 업데이트
-- 문제: 고객 ID가 5인 고객의 주소를 '123 New Address, New City'로 변경하시오.
-- 힌트:
-- UPDATE 구문을 사용하여 customer 테이블의 레코드를 업데이트합니다.
-- customer_id를 사용하여 특정 고객을 식별하고, address_id를 찾은 다음 address 테이블에서 해당 주소를 업데이트합니다.
-- 정답:
-- UPDATE customer
-- SET address_id = (SELECT address_id FROM address WHERE address = '123 New Address, New City')
-- WHERE customer_id = 5;

-- 영화 대여 상태 변경
-- 문제: 대여 ID가 200인 대여 기록의 상태를 'returned'로 변경하시오.
-- 힌트:
-- UPDATE 구문을 사용하여 rental 테이블의 레코드를 업데이트합니다.
-- rental_id를 사용하여 특정 대여 기록을 식별하고, return_date를 현재 날짜/시간으로 설정합니다.
-- 정답:
-- UPDATE rental
-- SET return_date = NOW()
-- WHERE rental_id = 200;

-- 배우 정보 삭제
-- 문제: 배우 ID가 10인 배우의 정보를 삭제하시오.
-- 힌트:
-- DELETE FROM 구문을 사용하여 actor 테이블에서 특정 레코드를 삭제합니다.
-- 삭제하기 전에 film_actor 테이블에서 해당 배우와 관련된 모든 레코드를 삭제하거나 확인합니다.
-- 정답:
-- DELETE FROM actor
-- WHERE actor_id = 10;