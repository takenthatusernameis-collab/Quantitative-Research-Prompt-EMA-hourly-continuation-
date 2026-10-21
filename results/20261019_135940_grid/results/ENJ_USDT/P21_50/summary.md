# EMA Hourly Continuation — ENJ/USDT P21_50

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1003 |
| net_profit_factor | 0.4932 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.9226 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -7.6281 |
| sortino_ratio | -3.4064 |
| max_drawdown | 0.9855 |
| cagr | -0.8121 |
| net_avg_win | 21.2628 |
| net_avg_loss | -35.2211 |
| avg_hold_time_bars | 4.2891 |
| exposure | 0.1947 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
