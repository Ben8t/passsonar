-- WITH full_pass AS (
-- 	SELECT * FROM event_pass
-- 	WHERE game_id = '4ee231f477be8a1e81a2668ec42ead31'
-- )

-- SELECT 
-- 	game_id,
-- 	team_id,
-- 	compute.player_id,
-- 	player_name,
-- 	angle,
-- 	COUNT(angle) AS freq,
-- 	AVG(distance) AS distance
-- FROM (
-- 	SELECT
-- 		game_id,
-- 		team_id,
-- 		player_id,
-- 		x_begin,
-- 		y_begin,
-- 		x_end,
-- 		y_end,
-- 		SQRT(POWER((y_end - y_begin),2) + POWER((x_end - x_begin),2)) AS distance,
-- 		-15 * ROUND((ATAN2((y_end - y_begin), (x_end - x_begin)) * 180 / PI())/15) AS angle
-- 	FROM full_pass
-- ) AS compute
-- INNER JOIN (SELECT DISTINCT player_id, player_name FROM player_base) AS player_base
-- ON compute.player_id = player_base.player_id
-- WHERE angle IS NOT NULL
-- GROUP BY game_id, team_id, compute.player_id, player_name, angle
-- ORDER BY team_id, compute.player_id, angle


WITH full_pass AS (
	SELECT * FROM event_pass
	WHERE game_id = '02928d2e2893b5e9fba2d0e52f42d768'
)

SELECT
	full_pass.game_id,
	full_pass.team_id,
	teams.team_name,
	full_pass.player_id,
	player_base.player_name,
	lineup_horizontal,
	lineup_vertical,
	x_begin,
	y_begin,
	x_end,
	y_end
FROM full_pass
INNER JOIN (SELECT DISTINCT player_id, player_name FROM player_base) AS player_base
ON full_pass.player_id = player_base.player_id
INNER JOIN (SELECT DISTINCT home_team_id AS team_id, home_team_name AS team_name FROM metadata) AS teams
ON full_pass.team_id = teams.team_id
INNER JOIN (SELECT DISTINCT player_id, game_id, lineup_vertical, lineup_horizontal FROM lineup) AS lineups
ON full_pass.game_id = lineups.game_id AND full_pass.player_id = lineups.player_id
ORDER BY team_id, full_pass.player_id
