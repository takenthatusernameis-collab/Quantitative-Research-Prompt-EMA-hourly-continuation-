# EMA Hourly Continuation — PIXEL/USDT P100_200

**Symbol:** PIXEL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.5891 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.8180 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -3.1301 |
| sortino_ratio | -0.8101 |
| max_drawdown | 0.6211 |
| cagr | -0.3168 |
| net_avg_win | 59.8250 |
| net_avg_loss | -79.5204 |
| avg_hold_time_bars | 12.2878 |
| exposure | 0.1874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
