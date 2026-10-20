# EMA Hourly Continuation — ORDI/USDT P20_34

**Symbol:** ORDI/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1191 |
| net_profit_factor | 0.4262 |
| net_win_rate | 0.4223 |
| gross_profit_factor | 0.8862 |
| gross_win_rate | 0.4400 |
| sharpe_ratio | -9.9871 |
| sortino_ratio | -4.8732 |
| max_drawdown | 0.9978 |
| cagr | -0.9124 |
| net_avg_win | 14.7357 |
| net_avg_loss | -25.2761 |
| avg_hold_time_bars | 2.4962 |
| exposure | 0.1351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
