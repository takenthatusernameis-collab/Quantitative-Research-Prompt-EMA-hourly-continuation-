# EMA Hourly Continuation — EIGEN/USDT P100_144

**Symbol:** EIGEN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 175 |
| net_profit_factor | 0.7394 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9233 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -1.3988 |
| sortino_ratio | -0.2923 |
| max_drawdown | 0.2676 |
| cagr | -0.1261 |
| net_avg_win | 81.6059 |
| net_avg_loss | -101.8715 |
| avg_hold_time_bars | 5.7029 |
| exposure | 0.0555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
