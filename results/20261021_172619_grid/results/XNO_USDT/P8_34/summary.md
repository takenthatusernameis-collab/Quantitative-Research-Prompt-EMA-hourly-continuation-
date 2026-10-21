# EMA Hourly Continuation — XNO/USDT P8_34

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.6538 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.8630 |
| gross_win_rate | 0.4429 |
| sharpe_ratio | -4.3395 |
| sortino_ratio | -1.6732 |
| max_drawdown | 0.8617 |
| cagr | -0.5372 |
| net_avg_win | 49.5672 |
| net_avg_loss | -60.2799 |
| avg_hold_time_bars | 7.6209 |
| exposure | 0.2550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
