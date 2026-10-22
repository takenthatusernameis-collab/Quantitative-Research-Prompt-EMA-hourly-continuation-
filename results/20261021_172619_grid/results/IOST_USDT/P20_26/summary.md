# EMA Hourly Continuation — IOST/USDT P20_26

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.5779 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9851 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -3.5261 |
| sortino_ratio | -0.9360 |
| max_drawdown | 0.6645 |
| cagr | -0.3502 |
| net_avg_win | 55.8742 |
| net_avg_loss | -89.0006 |
| avg_hold_time_bars | 4.4497 |
| exposure | 0.0684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
