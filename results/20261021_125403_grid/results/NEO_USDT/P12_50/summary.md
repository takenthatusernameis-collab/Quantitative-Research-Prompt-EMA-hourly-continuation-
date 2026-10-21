# EMA Hourly Continuation — NEO/USDT P12_50

**Symbol:** NEO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.6360 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.8670 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -3.5430 |
| sortino_ratio | -1.2663 |
| max_drawdown | 0.7673 |
| cagr | -0.4400 |
| net_avg_win | 45.7366 |
| net_avg_loss | -63.0834 |
| avg_hold_time_bars | 11.5710 |
| exposure | 0.3298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
