import styled from "styled-components";
import React from "react";
import { Pad } from "../Pad";
import { Center } from "../Center";
import { Layers } from "../Layers";
import Info from "./Info";
import Header from "./Header";
import { useParams } from "react-router-dom";
import { useFetchMeterByIdQuery } from "../../redux/services/meters";

const ContentArea = styled(Pad).attrs(() => ({
  padding: "1rem 0",
  margin: "2rem 0",
}))`
  background: rgb(1, 95, 156);
`;

const ContentCenter = styled(Center).attrs(() => ({
  as: Layers,
  gutter: "2rem",
  maxWidth: "50%",
}))`
  @media (max-width: 1000px) {
    max-inline-size: 70%;
  }
  @media (max-width: 700px) {
    max-inline-size: 94%;
  }
`;

const SettingPane = styled(Pad).attrs(() => ({
  padding: "1rem",
}))`
  background: white;
  border-radius: 0.4rem;
`;

export default function Content() {
  const { uuid } = useParams();
  const { data: meterById, isLoading, error } = useFetchMeterByIdQuery(uuid);

  return (
    <ContentArea>
      <ContentCenter>
        <SettingPane>
          {isLoading ? (
            <h3>Загрузка данных</h3>
          ) : error?.status === 404 || error?.status === "FETCH_ERROR" ? (
            <h3>Средство измерения не найдено</h3>
          ) : (
            <React.Fragment>
              <Header meterById={meterById} />
              <Info meterById={meterById} />
            </React.Fragment>
          )}
        </SettingPane>
      </ContentCenter>
    </ContentArea>
  );
}
