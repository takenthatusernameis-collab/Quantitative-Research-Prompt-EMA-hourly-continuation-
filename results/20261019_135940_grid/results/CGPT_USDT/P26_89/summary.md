# EMA Hourly Continuation — CGPT/USDT P26_89

**Symbol:** CGPT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.6065 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.9156 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -4.4623 |
| sortino_ratio | -1.5959 |
| max_drawdown | 0.8596 |
| cagr | -0.5424 |
| net_avg_win | 44.1643 |
| net_avg_loss | -61.7091 |
| avg_hold_time_bars | 10.0657 |
| exposure | 0.2992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
