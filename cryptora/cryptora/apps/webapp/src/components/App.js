import React, { Component } from "react";
import ReactDOM from "react-dom";

//import logo from './../../../../static/apple-touch-icon.png';
import './../../../../static/css/main.css';

const welcome = "Welcome to React"

class App extends Component {

    render() {
        return(
            <div className="App">
                <header className="App-header">
                    <img src="" className="App-logo"/>
                    <Welcome/>
                    </header>
            </div>

        )
    }

}

class Welcome extends Component {
    render(){
       return( <h1 className="App-title">{welcome}</h1>)
    }
}

export default App;



// import DataProvider from "./DataProvider";
// import Table from "./Table";

// const App = () => (
//   <DataProvider endpoint="/api/transactions/"
//                 render={data => <Table data={data} />} />
// );
// const wrapper = document.getElementById("app");
// wrapper ? ReactDOM.render(<App />, wrapper) : null;

