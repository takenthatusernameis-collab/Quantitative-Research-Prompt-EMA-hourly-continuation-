# EMA Hourly Continuation — SAFE/USDT P21_26

**Symbol:** SAFE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1108 |
| net_profit_factor | 0.2146 |
| net_win_rate | 0.3664 |
| gross_profit_factor | 0.6684 |
| gross_win_rate | 0.4170 |
| sharpe_ratio | -13.1429 |
| sortino_ratio | -6.3212 |
| max_drawdown | 0.9998 |
| cagr | -0.9652 |
| net_avg_win | 6.7287 |
| net_avg_loss | -18.1333 |
| avg_hold_time_bars | 2.8348 |
| exposure | 0.1438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
