# EMA Hourly Continuation — WLD/USDT P20_50

**Symbol:** WLD/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.8010 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9944 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.4683 |
| sortino_ratio | -0.4418 |
| max_drawdown | 0.4229 |
| cagr | -0.1845 |
| net_avg_win | 73.3530 |
| net_avg_loss | -91.1612 |
| avg_hold_time_bars | 9.8776 |
| exposure | 0.1980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
