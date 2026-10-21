# EMA Hourly Continuation — ANYONE/USDT P21_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.8479 |
| net_win_rate | 0.4936 |
| gross_profit_factor | 0.9608 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -0.9162 |
| sortino_ratio | -0.2433 |
| max_drawdown | 0.2841 |
| cagr | -0.1087 |
| net_avg_win | 82.8458 |
| net_avg_loss | -95.2305 |
| avg_hold_time_bars | 33.8205 |
| exposure | 0.5332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
