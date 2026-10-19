# EMA Hourly Continuation — WIF/USDT P21_50

**Symbol:** WIF/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1010 |
| net_profit_factor | 0.6474 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9839 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -5.5946 |
| sortino_ratio | -2.5061 |
| max_drawdown | 0.9536 |
| cagr | -0.7004 |
| net_avg_win | 36.4785 |
| net_avg_loss | -50.8258 |
| avg_hold_time_bars | 4.3277 |
| exposure | 0.1987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
