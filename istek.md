@import "compass";

@function createShadow($shadowsCount, $radius, $color, $startAngle) {
  $sh: "0px 0px 0px transparent";
  $angle: $startAngle / $shadowsCount;
  @for $i from 1 through $shadowsCount {
    $x: $radius * cos($angle * $i);
    $y: $radius * sin($angle * $i);
    $sh: "#{$sh}, #{$x} #{$y} #{$color}";
  }
  @return unquote($sh);
}

html,
body {
  height: 100%;
  width: 100%;
  --background-color: #212752;
}
body {
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--background-color);
}
.avatar {
  --border-color: #4255d4;
  --background-color: #212752;
  --avatar-size: 150px;
  height: var(--avatar-size);
  width: var(--avatar-size);
  border: 4px solid var(--border-color);
  padding: 6px;
  border-radius: 50%;
  position: relative;
  &::before,
  &::after {
    content: "";
    position: absolute;
    height: 6px;
    width: 6px;
    // border-radius: 100%;
    transform: rotate(45deg);
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    margin: auto;
  }
  &::before {
    box-shadow: createShadow(8, 7rem, #4255d4, 360deg);
    animation: animate-2 1s ease-in-out infinite;
  }
  &::after {
    box-shadow: createShadow(16, 6rem, #4255d4, 360deg);
    transform: rotate(12deg);
    animation: animate-1 1s ease-in-out infinite;
  }
  img {
    max-width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: inherit;
  }
}

@keyframes animate-1 {
  0%,
  100% {
    box-shadow: createShadow(16, 6rem, #4255d4, 360deg);
  }
  50% {
    box-shadow: createShadow(16, 5.5rem, #4255d4, 360deg);
  }
}

@keyframes animate-2 {
  0%,
  100% {
    box-shadow: createShadow(8, 5.5rem, #4255d4, 360deg);
  }
  50% {
    box-shadow: createShadow(8, 6rem, #4255d4, 360deg);
  }
}

/********************************/
.pens_link {
  position: fixed;
  bottom: 56px;
  right: 56px;
  margin: auto;
  display: inline-flex;
  font-size: 2rem;
  text-decoration: none;
  border-radius: 500px;
  background-color: #ffffff;
  color: #212121;
  height: 56px;
  width: 56px;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  animation: animate 1500ms ease infinite;
  @keyframes animate {
    0%,
    100% {
      transform: translatey(-10%);
    }
    50% {
      transform: translatey(10%);
    }
  }
}

/*******************************/




























<div class="avatar">
  <img src="https://images.unsplash.com/photo-1550314124-301ca0b773ae?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=2215&q=80" alt="">
</div>

<!-- ----------------------- -->
<a href="https://codepen.io/chandrashekhar" target="_blank" class="pens_link">
  <i class="fa-brands fa-codepen"></i>
</a>
<!-- ----------------------- -->