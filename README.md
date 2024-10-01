Task 3 - Create a React-Redux Application
================================

This project was given by [BlueOC Entrance Test](https://docs.google.com/document/d/1HK-Dye8jrWvFgMTHt24c76igX3yMcYj83CjYQhESUdQ/edit).

## Objectives
1. Uses Redux for state management and API calls.
2. Fetches and displays posts from the API.
3. Includes a PostForm component to add new posts.
4. Using ES6 syntax where applicable.

## The File System Directory for the Important Files
```
.
├── src
│   ├── actions
│   │   ├── postActions.js
│   │   └── types.js
│   ├── components
│   │   ├── Postform.js
│   │   └── Posts.js
│   └── reducers
│       ├── index.js
│       └── postReducer.js
├── App.css
├── index.js
├── store.js
└── README.md
```
## The Data Flow 
1. Store: The current state of the application at a specific time.
2. View: The state rendered the UI application.
3. Actions: The UI application gets updated actions via the input.
4. Store: The new state is updated in the UI application.
5. Reducers: The reducers calculate the new state value based on the state and action arguments -> Support Redux's scalable and predictable state management

## Available Commands to Run the Application
### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.
