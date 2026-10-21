# EMA Hourly Continuation — DCR/USDT P21_34

**Symbol:** DCR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.6764 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0482 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -2.6363 |
| sortino_ratio | -0.7946 |
| max_drawdown | 0.6358 |
| cagr | -0.3044 |
| net_avg_win | 56.2336 |
| net_avg_loss | -85.4296 |
| avg_hold_time_bars | 5.3318 |
| exposure | 0.1062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
