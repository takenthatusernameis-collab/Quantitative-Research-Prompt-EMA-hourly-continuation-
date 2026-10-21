# EMA Hourly Continuation — JTO/USDT P8_100

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.8051 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9375 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -1.5456 |
| sortino_ratio | -0.4981 |
| max_drawdown | 0.4954 |
| cagr | -0.2067 |
| net_avg_win | 73.7738 |
| net_avg_loss | -85.7281 |
| avg_hold_time_bars | 27.9198 |
| exposure | 0.6485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
