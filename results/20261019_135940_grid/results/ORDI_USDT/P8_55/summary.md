# EMA Hourly Continuation — ORDI/USDT P8_55

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1069 |
| net_profit_factor | 0.6503 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.9852 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -5.4284 |
| sortino_ratio | -2.4773 |
| max_drawdown | 0.9531 |
| cagr | -0.7005 |
| net_avg_win | 35.0399 |
| net_avg_loss | -48.2465 |
| avg_hold_time_bars | 10.2984 |
| exposure | 0.5004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
