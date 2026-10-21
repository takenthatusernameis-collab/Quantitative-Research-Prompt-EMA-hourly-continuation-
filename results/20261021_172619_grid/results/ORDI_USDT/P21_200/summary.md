# EMA Hourly Continuation — ORDI/USDT P21_200

**Symbol:** ORDI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7363 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8652 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -1.8651 |
| sortino_ratio | -0.4900 |
| max_drawdown | 0.4543 |
| cagr | -0.2022 |
| net_avg_win | 76.5001 |
| net_avg_loss | -88.7333 |
| avg_hold_time_bars | 36.3586 |
| exposure | 0.5669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
