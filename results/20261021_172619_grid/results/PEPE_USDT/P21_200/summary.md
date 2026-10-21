# EMA Hourly Continuation — PEPE/USDT P21_200

**Symbol:** PEPE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.8236 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9807 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -0.9346 |
| sortino_ratio | -0.2125 |
| max_drawdown | 0.2422 |
| cagr | -0.0943 |
| net_avg_win | 81.6134 |
| net_avg_loss | -98.3167 |
| avg_hold_time_bars | 57.0830 |
| exposure | 0.6565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
