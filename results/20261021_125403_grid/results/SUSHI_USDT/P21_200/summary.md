# EMA Hourly Continuation — SUSHI/USDT P21_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.8012 |
| net_win_rate | 0.4971 |
| gross_profit_factor | 0.9731 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -1.1873 |
| sortino_ratio | -0.3168 |
| max_drawdown | 0.3300 |
| cagr | -0.1370 |
| net_avg_win | 71.9174 |
| net_avg_loss | -88.7413 |
| avg_hold_time_bars | 36.8086 |
| exposure | 0.5830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
