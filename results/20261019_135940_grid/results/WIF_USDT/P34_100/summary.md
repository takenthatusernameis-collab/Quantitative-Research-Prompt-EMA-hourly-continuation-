# EMA Hourly Continuation — WIF/USDT P34_100

**Symbol:** WIF/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.6169 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.8831 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -4.2850 |
| sortino_ratio | -1.5791 |
| max_drawdown | 0.8520 |
| cagr | -0.5270 |
| net_avg_win | 43.0532 |
| net_avg_loss | -60.7740 |
| avg_hold_time_bars | 8.2526 |
| exposure | 0.2555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
