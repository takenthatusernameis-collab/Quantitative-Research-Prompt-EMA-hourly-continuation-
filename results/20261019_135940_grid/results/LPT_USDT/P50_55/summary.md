# EMA Hourly Continuation — LPT/USDT P50_55

**Symbol:** LPT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 885 |
| net_profit_factor | 0.2106 |
| net_win_rate | 0.3571 |
| gross_profit_factor | 0.5729 |
| gross_win_rate | 0.4339 |
| sharpe_ratio | -12.3159 |
| sortino_ratio | -5.3396 |
| max_drawdown | 0.9992 |
| cagr | -0.9417 |
| net_avg_win | 8.4336 |
| net_avg_loss | -22.2444 |
| avg_hold_time_bars | 2.1853 |
| exposure | 0.0879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
