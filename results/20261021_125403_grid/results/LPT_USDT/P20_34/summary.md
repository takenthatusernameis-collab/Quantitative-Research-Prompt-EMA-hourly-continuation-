# EMA Hourly Continuation — LPT/USDT P20_34

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6423 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.9225 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -3.3471 |
| sortino_ratio | -0.9825 |
| max_drawdown | 0.6933 |
| cagr | -0.3640 |
| net_avg_win | 61.8828 |
| net_avg_loss | -84.7391 |
| avg_hold_time_bars | 4.7530 |
| exposure | 0.0910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
