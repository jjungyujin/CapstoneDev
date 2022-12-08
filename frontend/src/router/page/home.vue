<script>
import mainHeader from "../../components/mainHeader";
import mainNav from "../../components/mainNav";
import mainDashboard from "../../components/mainDashboard";
import mainInputTableHeader from "../../components/mainInputTableHeader";
import mainInputTable from "../../components/mainInputTable";
import resetButton from "../../components/resetButton";
import predictButton from "../../components/predictButton";
import mainFooter from "../../components/mainFooter";

export default {
  components: {
    mainHeader,
    mainNav,
    mainDashboard,
    mainInputTableHeader,
    mainInputTable,
    resetButton,
    predictButton,
    mainFooter
  }
};
</script>

<template>
  <div>
    <mainHeader />
    <div id="layoutSidenav">
      <mainNav />
      <div id="layoutSidenav_content">
        <div class="container-fluid px-4">
          <mainDashboard />
          <div class="card mb-4">
            <mainInputTableHeader />
            <mainInputTable />
            <div class="main-input-table-button">
              <resetButton />
              <predictButton />
            </div>
          </div>
        </div>
        <mainFooter />
      </div>
    </div>
  </div>
</template>
