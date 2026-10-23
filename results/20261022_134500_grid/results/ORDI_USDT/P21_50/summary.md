# EMA Hourly Continuation — ORDI/USDT P21_50

**Symbol:** ORDI/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 993 |
| net_profit_factor | 0.5550 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.9438 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -6.6314 |
| sortino_ratio | -2.9358 |
| max_drawdown | 0.9732 |
| cagr | -0.7609 |
| net_avg_win | 26.4206 |
| net_avg_loss | -40.9212 |
| avg_hold_time_bars | 4.2840 |
| exposure | 0.1934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
