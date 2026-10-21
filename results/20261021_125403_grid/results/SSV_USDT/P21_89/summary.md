# EMA Hourly Continuation — SSV/USDT P21_89

**Symbol:** SSV/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.7523 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9313 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -2.2529 |
| sortino_ratio | -0.7393 |
| max_drawdown | 0.6134 |
| cagr | -0.2886 |
| net_avg_win | 68.9156 |
| net_avg_loss | -83.3990 |
| avg_hold_time_bars | 14.9887 |
| exposure | 0.3615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
