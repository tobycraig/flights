match ({name:'Edinburgh'})--(destination)-[f]-({name:'Stockholm'}) where f.airline='Norwegian Air Shuttle' return distinct destination order by destination.name
