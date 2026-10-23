# EMA Hourly Continuation — PUNDIX/USDT P8_200

**Symbol:** PUNDIX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6598 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -2.5595 |
| sortino_ratio | -0.7265 |
| max_drawdown | 0.6033 |
| cagr | -0.2938 |
| net_avg_win | 57.0770 |
| net_avg_loss | -81.5588 |
| avg_hold_time_bars | 42.5833 |
| exposure | 0.7897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
