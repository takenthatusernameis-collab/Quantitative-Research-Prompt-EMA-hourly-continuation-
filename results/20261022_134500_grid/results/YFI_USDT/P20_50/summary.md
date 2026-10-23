# EMA Hourly Continuation — YFI/USDT P20_50

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1148 |
| net_profit_factor | 0.4400 |
| net_win_rate | 0.4303 |
| gross_profit_factor | 1.0538 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -10.1848 |
| sortino_ratio | -4.8714 |
| max_drawdown | 0.9982 |
| cagr | -0.9155 |
| net_avg_win | 15.8745 |
| net_avg_loss | -27.2513 |
| avg_hold_time_bars | 4.4225 |
| exposure | 0.2297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
