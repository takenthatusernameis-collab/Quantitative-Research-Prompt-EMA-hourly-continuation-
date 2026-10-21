# EMA Hourly Continuation — GMX/USDT P12_26

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.6522 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9555 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -3.4644 |
| sortino_ratio | -1.2384 |
| max_drawdown | 0.7580 |
| cagr | -0.4316 |
| net_avg_win | 47.2124 |
| net_avg_loss | -68.0959 |
| avg_hold_time_bars | 6.2319 |
| exposure | 0.1759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
