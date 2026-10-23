# EMA Hourly Continuation — QI/USDT P26_50

**Symbol:** QI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.4778 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.9413 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -6.8667 |
| sortino_ratio | -2.8969 |
| max_drawdown | 0.9722 |
| cagr | -0.7553 |
| net_avg_win | 21.6255 |
| net_avg_loss | -38.5914 |
| avg_hold_time_bars | 4.0896 |
| exposure | 0.1653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
