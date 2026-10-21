# EMA Hourly Continuation — LUNC/USDT P34_144

**Symbol:** LUNC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.7553 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 0.9791 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -1.6129 |
| sortino_ratio | -0.4565 |
| max_drawdown | 0.4385 |
| cagr | -0.1896 |
| net_avg_win | 64.5726 |
| net_avg_loss | -85.9351 |
| avg_hold_time_bars | 19.7442 |
| exposure | 0.3509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
