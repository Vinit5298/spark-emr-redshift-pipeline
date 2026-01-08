-- Phase 5: Merge users from staging to final table

BEGIN;

DELETE FROM public.users_final
USING public.users_stage
WHERE users_final.user_id = users_stage.user_id;

INSERT INTO public.users_final
SELECT * FROM public.users_stage;

TRUNCATE TABLE public.users_stage;

COMMIT;

SELECT * FROM public.users_final;
