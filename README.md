![th-sklearn-iris-demo-cover](https://media-blog.sashido.io/content/images/2021/08/th-sklearn-iris-demo-cover.jpeg)

# Local Development

# Deploy on Heroku

Heroku is a free hosting service for hosting small projects. Easy setup and deploy from the command line via git.

## Install Heroku

1. Create an account on https://heroku.com. This should be pretty straight forward.
2. Install the Heroku CLI on your computer: [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli).

After completing the steps above, check that you have the `heroku-cli` installed by checking the version number in your terminal:

```
heroku --version
```

3. Connect the `Heroku CLI` to your account by writing the following command in your terminal and follow the instructions on the command line:

```
heroku login
```

## Deploy

1. ...


2. Create a remote heroku project, kinda like creating a git repository on GitHub. This will create a project on Heroku with a random name. If you want to name your app you have to supply your own name like `heroku create project-name`. The command below will just create a random name:

```
heroku create
```

3. Push your app to **Heroku** like pushing to GitHub expect for `origin` you have `heroku` (you will see a wall of code).

```
git push heroku master
```

4. Visit your newly create app by opening it via heroku:

```
heroku open
```

If you are getting errors you can view the error logs by running this command:

```
heroku logs --tail
```
