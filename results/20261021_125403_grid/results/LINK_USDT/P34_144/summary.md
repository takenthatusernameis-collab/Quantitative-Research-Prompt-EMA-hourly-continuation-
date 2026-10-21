# EMA Hourly Continuation — LINK/USDT P34_144

**Symbol:** LINK/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.8557 |
| net_win_rate | 0.5249 |
| gross_profit_factor | 1.1004 |
| gross_win_rate | 0.5249 |
| sharpe_ratio | -0.8622 |
| sortino_ratio | -0.2293 |
| max_drawdown | 0.2938 |
| cagr | -0.1016 |
| net_avg_win | 78.2116 |
| net_avg_loss | -100.9868 |
| avg_hold_time_bars | 23.1554 |
| exposure | 0.3589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
