# EMA Hourly Continuation — BLUR/USDT P50_89

**Symbol:** BLUR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.6105 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 1.0510 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -4.6952 |
| sortino_ratio | -1.6856 |
| max_drawdown | 0.8823 |
| cagr | -0.5549 |
| net_avg_win | 44.1391 |
| net_avg_loss | -66.0988 |
| avg_hold_time_bars | 5.0603 |
| exposure | 0.1482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
