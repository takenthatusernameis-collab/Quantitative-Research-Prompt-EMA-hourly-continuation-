# EMA Hourly Continuation — ONT/USDT P21_89

**Symbol:** ONT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.7609 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9687 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -2.0156 |
| sortino_ratio | -0.6402 |
| max_drawdown | 0.5796 |
| cagr | -0.2560 |
| net_avg_win | 68.8532 |
| net_avg_loss | -86.5694 |
| avg_hold_time_bars | 16.1429 |
| exposure | 0.3630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
