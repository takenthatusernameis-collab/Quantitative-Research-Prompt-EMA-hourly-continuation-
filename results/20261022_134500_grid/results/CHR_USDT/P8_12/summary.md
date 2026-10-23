# EMA Hourly Continuation — CHR/USDT P8_12

**Symbol:** CHR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1749 |
| net_profit_factor | 0.2519 |
| net_win_rate | 0.3808 |
| gross_profit_factor | 0.7124 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -15.2795 |
| sortino_ratio | -9.1572 |
| max_drawdown | 1.0000 |
| cagr | -0.9905 |
| net_avg_win | 5.0557 |
| net_avg_loss | -12.3426 |
| avg_hold_time_bars | 2.3128 |
| exposure | 0.1830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
