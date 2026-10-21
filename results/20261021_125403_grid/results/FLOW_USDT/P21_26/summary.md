# EMA Hourly Continuation — FLOW/USDT P21_26

**Symbol:** FLOW/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 186 |
| net_profit_factor | 0.5515 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.8285 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -2.5112 |
| sortino_ratio | -0.4906 |
| max_drawdown | 0.4657 |
| cagr | -0.2011 |
| net_avg_win | 63.0725 |
| net_avg_loss | -94.1863 |
| avg_hold_time_bars | 4.5968 |
| exposure | 0.0389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
