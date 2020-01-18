WITH full_pass AS (
	SELECT * FROM event_pass
	WHERE game_id = '4ee231f477be8a1e81a2668ec42ead31'
)

SELECT 
	game_id,
	team_id,
	compute.player_id,
	player_name,
	angle,
	COUNT(angle) AS freq,
	AVG(distance) AS distance
FROM (
	SELECT
		game_id,
		team_id,
		player_id,
		x_begin,
		y_begin,
		x_end,
		y_end,
		SQRT(POWER((y_end - y_begin),2) + POWER((x_end - x_begin),2)) AS distance,
		-15 * ROUND((ATAN2((y_end - y_begin), (x_end - x_begin)) * 180 / PI())/15) AS angle
	FROM full_pass
) AS compute
INNER JOIN (SELECT DISTINCT player_id, player_name FROM player_base) AS player_base
ON compute.player_id = player_base.player_id
WHERE angle IS NOT NULL
GROUP BY game_id, team_id, compute.player_id, player_name, angle
ORDER BY team_id, compute.player_id, angle


-- WITH full_pass AS (
-- 	SELECT * FROM event_pass
-- 	WHERE player_id = '89925'
-- )

-- SELECT
-- 	game_id,
-- 	team_id,
-- 	full_pass.player_id,
-- 	x_begin,
-- 	y_begin,
-- 	x_end,
-- 	y_end
-- FROM full_pass
-- INNER JOIN (SELECT DISTINCT player_id, player_name FROM player_base) AS player_base
-- ON full_pass.player_id = player_base.player_id
-- ORDER BY team_id, full_pass.player_id
