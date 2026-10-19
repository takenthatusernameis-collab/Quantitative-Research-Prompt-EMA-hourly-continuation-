# EMA Hourly Continuation — AERO/USDT P21_200

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.8012 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 1.0209 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3887 |
| sortino_ratio | -0.3547 |
| max_drawdown | 0.4170 |
| cagr | -0.1540 |
| net_avg_win | 86.3863 |
| net_avg_loss | -106.4915 |
| avg_hold_time_bars | 43.0497 |
| exposure | 0.6301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
