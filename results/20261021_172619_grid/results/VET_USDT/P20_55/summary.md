# EMA Hourly Continuation — VET/USDT P20_55

**Symbol:** VET/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7899 |
| net_win_rate | 0.5178 |
| gross_profit_factor | 1.0878 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -1.8296 |
| sortino_ratio | -0.6076 |
| max_drawdown | 0.5296 |
| cagr | -0.2440 |
| net_avg_win | 68.7471 |
| net_avg_loss | -93.4636 |
| avg_hold_time_bars | 7.8349 |
| exposure | 0.1898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
