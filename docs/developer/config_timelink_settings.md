
## Configuring `timelink` 

`timelink` uses `Pydantic-settings` to manage package and application settings.
See https://docs.pydantic.dev/latest/concepts/pydantic_settings/

This allows to manage effortlessly default values, `.env`  files and environment variables.

The class `WebAppSettings` in  `timelink/app/backend/webapp_settings.py` defines default values for `Timelink` web application.

In code the default values can be overridden when creating an instance:

        settings = WebAppSettings(timelink_admin_pwd="xpto", time_user_db_type="postgres")

Or values can be read from a `.env` file:

	 settings = WebAppSettings(_envfile='.)

- See https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support

Or from arguments in the command line.

- See https://docs.pydantic.dev/latest/concepts/pydantic_settings/#command-line-support








