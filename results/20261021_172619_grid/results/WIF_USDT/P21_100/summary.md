# EMA Hourly Continuation — WIF/USDT P21_100

**Symbol:** WIF/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.8855 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0379 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -0.7815 |
| sortino_ratio | -0.2347 |
| max_drawdown | 0.3521 |
| cagr | -0.1063 |
| net_avg_win | 84.9063 |
| net_avg_loss | -100.3654 |
| avg_hold_time_bars | 18.7283 |
| exposure | 0.3729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
