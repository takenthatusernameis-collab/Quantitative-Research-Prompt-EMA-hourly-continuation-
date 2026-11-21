# EMA Hourly Continuation — HTR/USDT P8_100

**Symbol:** HTR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 868 |
| net_profit_factor | 0.5099 |
| net_win_rate | 0.3929 |
| gross_profit_factor | 0.7184 |
| gross_win_rate | 0.4032 |
| sharpe_ratio | -7.2781 |
| sortino_ratio | -2.9977 |
| max_drawdown | 0.9748 |
| cagr | -0.7688 |
| net_avg_win | 29.7407 |
| net_avg_loss | -37.7396 |
| avg_hold_time_bars | 14.5115 |
| exposure | 0.5725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
