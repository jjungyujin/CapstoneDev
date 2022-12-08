<template>
  <div>
    <h1 class="mt-4">Prediction</h1>
    <ol class="breadcrumb mb-4">
      <li class="breadcrumb-item active">
        입력한 파라미터로 압연 공정을 진행했을 때 나오는 코일의 두께를
        예측합니다.
      </li>
    </ol>
    <div class="card mb-4">
      <div class="card-body">
        압연공정의 기본 정보를 입력해주세요.<br /><br />
        <label for="workerName">작업자명 :</label>
        <select id="workerName" class="basic-info-selector" name="workerName">
          <option value="syd">서용득</option>
          <option value="jsw">조성우</option>
          <option value="jyj" selected>정유진</option>
          <option value="ljh">이정화</option>
        </select>
        <label for="rollingMillNum">압연기 번호 :</label>
        <select
          id="rollingMillNum"
          class="basic-info-selector"
          name="rollingMillNum"
        >
          <option value="1CRM">1CRM</option>
          <option value="2CRM" selected>2CRM</option>
          <option value="3CRM">3CRM</option>
        </select>
        <label for="coilNum">코일 번호 :</label>
        <select id="coilNum" class="basic-info-selector" name="coilNum">
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3" selected>3</option>
          <option value="4">4</option>
        </select>
      </div>
    </div>
  </div>
</template>
