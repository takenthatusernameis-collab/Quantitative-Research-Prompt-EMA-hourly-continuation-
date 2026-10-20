# EMA Hourly Continuation — XPR/USDT P50_89

**Symbol:** XPR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.3315 |
| net_win_rate | 0.3723 |
| gross_profit_factor | 0.6945 |
| gross_win_rate | 0.3906 |
| sharpe_ratio | -9.2878 |
| sortino_ratio | -3.4187 |
| max_drawdown | 0.9884 |
| cagr | -0.8289 |
| net_avg_win | 19.9981 |
| net_avg_loss | -35.7889 |
| avg_hold_time_bars | 4.1778 |
| exposure | 0.1250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
