# EMA Hourly Continuation — ANYONE/USDT P89_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.5477 |
| net_win_rate | 0.4477 |
| gross_profit_factor | 0.7865 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -3.9380 |
| sortino_ratio | -1.1892 |
| max_drawdown | 0.7369 |
| cagr | -0.4325 |
| net_avg_win | 47.5130 |
| net_avg_loss | -70.3120 |
| avg_hold_time_bars | 6.7908 |
| exposure | 0.1410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
