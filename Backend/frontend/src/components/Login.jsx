

const Login = ()=>{
   
    return(
    <div className="container">
<div className="login-box">
  <h2>Login</h2>
  <form action="#">
    <div className="input-box">
      <input type="email" required="" />
      <label>Email</label>
    </div>
    <div className="input-box">
      <input type="password" required="" />
      <label>Password</label>
    </div>
    <div className="forgot-pass">
      <a href="#">Forgot your password?</a>
    </div>
    <button type="submit" className="btn">
      Login
    </button>
    <div className="signup-link">
      <a href="/register">Signup</a>
    </div>
  </form>
</div>
</div>
);}

export default Login;