# EMA Hourly Continuation — BAND/USDT P12_26

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1226 |
| net_profit_factor | 0.4105 |
| net_win_rate | 0.4421 |
| gross_profit_factor | 0.9026 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -9.2446 |
| sortino_ratio | -4.5544 |
| max_drawdown | 0.9967 |
| cagr | -0.8964 |
| net_avg_win | 12.8041 |
| net_avg_loss | -24.7179 |
| avg_hold_time_bars | 3.8940 |
| exposure | 0.2160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
