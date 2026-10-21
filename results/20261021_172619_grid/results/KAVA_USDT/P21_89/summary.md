# EMA Hourly Continuation — KAVA/USDT P21_89

**Symbol:** KAVA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.6421 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.8935 |
| gross_win_rate | 0.4631 |
| sharpe_ratio | -3.6787 |
| sortino_ratio | -1.2018 |
| max_drawdown | 0.7674 |
| cagr | -0.4292 |
| net_avg_win | 55.7572 |
| net_avg_loss | -73.7855 |
| avg_hold_time_bars | 16.3157 |
| exposure | 0.3923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
