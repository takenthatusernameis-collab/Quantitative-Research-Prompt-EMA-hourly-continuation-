# EMA Hourly Continuation — AMP/USDT P12_89

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.5431 |
| net_win_rate | 0.4127 |
| gross_profit_factor | 0.7032 |
| gross_win_rate | 0.4127 |
| sharpe_ratio | -4.9134 |
| sortino_ratio | -1.7660 |
| max_drawdown | 0.8736 |
| cagr | -0.5574 |
| net_avg_win | 38.7706 |
| net_avg_loss | -50.1588 |
| avg_hold_time_bars | 15.6600 |
| exposure | 0.4605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
