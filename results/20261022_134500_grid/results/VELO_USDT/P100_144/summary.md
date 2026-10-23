# EMA Hourly Continuation — VELO/USDT P100_144

**Symbol:** VELO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.6402 |
| net_win_rate | 0.5089 |
| gross_profit_factor | 1.0227 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -3.0821 |
| sortino_ratio | -0.9838 |
| max_drawdown | 0.7109 |
| cagr | -0.3720 |
| net_avg_win | 47.7059 |
| net_avg_loss | -77.2229 |
| avg_hold_time_bars | 3.9208 |
| exposure | 0.0900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
