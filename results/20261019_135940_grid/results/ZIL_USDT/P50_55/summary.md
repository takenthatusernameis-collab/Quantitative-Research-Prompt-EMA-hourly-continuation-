# EMA Hourly Continuation — ZIL/USDT P50_55

**Symbol:** ZIL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 853 |
| net_profit_factor | 0.1651 |
| net_win_rate | 0.3576 |
| gross_profit_factor | 0.6659 |
| gross_win_rate | 0.4197 |
| sharpe_ratio | -12.9389 |
| sortino_ratio | -5.6118 |
| max_drawdown | 0.9995 |
| cagr | -0.9531 |
| net_avg_win | 6.4817 |
| net_avg_loss | -21.8473 |
| avg_hold_time_bars | 1.8921 |
| exposure | 0.0734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
