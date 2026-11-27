# EMA Hourly Continuation — SHR/USDT P50_55

**Symbol:** SHR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 993 |
| net_profit_factor | 0.1824 |
| net_win_rate | 0.2558 |
| gross_profit_factor | 0.4180 |
| gross_win_rate | 0.2749 |
| sharpe_ratio | -14.8313 |
| sortino_ratio | -6.7408 |
| max_drawdown | 0.9999 |
| cagr | -0.9712 |
| net_avg_win | 8.7801 |
| net_avg_loss | -16.5478 |
| avg_hold_time_bars | 2.3807 |
| exposure | 0.1070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
