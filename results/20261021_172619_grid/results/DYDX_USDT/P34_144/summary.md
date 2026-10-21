# EMA Hourly Continuation — DYDX/USDT P34_144

**Symbol:** DYDX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.9744 |
| net_win_rate | 0.5436 |
| gross_profit_factor | 1.1759 |
| gross_win_rate | 0.5436 |
| sharpe_ratio | -0.1058 |
| sortino_ratio | -0.0284 |
| max_drawdown | 0.2202 |
| cagr | -0.0190 |
| net_avg_win | 95.8848 |
| net_avg_loss | -117.2042 |
| avg_hold_time_bars | 26.3605 |
| exposure | 0.4122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
