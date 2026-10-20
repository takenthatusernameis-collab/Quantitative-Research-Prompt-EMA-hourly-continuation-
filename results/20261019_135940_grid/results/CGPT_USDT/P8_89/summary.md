# EMA Hourly Continuation — CGPT/USDT P8_89

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.7182 |
| net_win_rate | 0.5113 |
| gross_profit_factor | 1.0655 |
| gross_win_rate | 0.5240 |
| sharpe_ratio | -2.6114 |
| sortino_ratio | -0.9801 |
| max_drawdown | 0.7067 |
| cagr | -0.3754 |
| net_avg_win | 48.8143 |
| net_avg_loss | -71.1093 |
| avg_hold_time_bars | 19.6695 |
| exposure | 0.6330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
