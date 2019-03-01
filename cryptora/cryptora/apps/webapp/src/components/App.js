import React, { Component } from "react";
import "~ css/main.css";
import Logo from '~ media/logo.svg';


const welcome = "Welcome to Cryptopia";

class App extends Component {

    render() {
        return(
            <Row />
        )
    }

}

class Welcome extends Component {
    render(){
       return(
           <div className="columns App">
               <div className="columns">
                   <header className="App-header">
                       <Logo width={40} height={40} className="App-logo" alt="logo"/>
                       <h1 className="App-title">{welcome}</h1>)
                   </header>
                   <p className="App-intro"> Cryptora in the house </p>
               </div>
           </div>
       )
    }
}

class Row extends Component {
    render() {
        return (
            <div className="column">
                <div className="columns is-desktop">
                    <div className="column App-box">
                        <p className="App-box">
                            One
                        </p>
                    </div>
                    <div className="column App-box">
                        <p className="App-box">
                            Two
                        </p>
                    </div>
                    <div className="column App-box">
                        <p className="App-box">
                            Three
                        </p>
                    </div>
                    <div className="column App-box">
                        <p className="App-box">
                            Four
                        </p>
                    </div>
                </div>
            </div>
        )
    }
}

export default App;