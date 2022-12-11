<template>
  <div id="layoutSidenav_nav">
    <nav class="sb-sidenav accordion sb-sidenav-dark" id="sidenavAccordion">
      <div class="sb-sidenav-menu">
        <div class="nav">
          <div class="sb-sidenav-menu-heading">Menu</div>
          <a class="nav-link" @click="toPredicton">
            <div class="sb-nav-link-icon">
              <i class="fas fa-tachometer-alt"></i>
            </div>
            Prediction
          </a>
          <a class="nav-link" @click="toHistory">
            <div class="sb-nav-link-icon">
              <i class="fas fa-tachometer-alt"></i>
            </div>
            History
          </a>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>

export default {
  name: "mainNav",
  methods: {
    toPredicton() {
      this.$router.push('/');
    },
    toHistory() {
      this.$router.push('/history');
    }
  }
}
</script>
