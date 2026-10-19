# EMA Hourly Continuation — JUP/USDT P21_55

**Symbol:** JUP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 906 |
| net_profit_factor | 0.5776 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9330 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -5.2760 |
| sortino_ratio | -2.2418 |
| max_drawdown | 0.9355 |
| cagr | -0.6579 |
| net_avg_win | 29.6525 |
| net_avg_loss | -46.3750 |
| avg_hold_time_bars | 5.4735 |
| exposure | 0.2254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
