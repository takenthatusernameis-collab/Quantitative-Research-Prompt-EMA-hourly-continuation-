# EMA Hourly Continuation — LPT/USDT P20_50

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.6682 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.8906 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -3.4734 |
| sortino_ratio | -1.1901 |
| max_drawdown | 0.7572 |
| cagr | -0.4216 |
| net_avg_win | 56.1448 |
| net_avg_loss | -72.6386 |
| avg_hold_time_bars | 7.2664 |
| exposure | 0.1909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
