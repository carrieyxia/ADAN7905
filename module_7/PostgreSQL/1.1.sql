SELECT 
    actor.actor_id,
    actor.first_name,
    actor.last_name,
    COUNT(rental.rental_id) AS rental_count
FROM 
    actor
JOIN 
    film_actor ON actor.actor_id = film_actor.actor_id
JOIN 
    film ON film_actor.film_id = film.film_id
JOIN 
    inventory ON film.film_id = inventory.film_id
JOIN 
    rental ON inventory.inventory_id = rental.inventory_id
GROUP BY 
    actor.actor_id, actor.first_name, actor.last_name
ORDER BY 
    rental_count DESC
LIMIT 10;