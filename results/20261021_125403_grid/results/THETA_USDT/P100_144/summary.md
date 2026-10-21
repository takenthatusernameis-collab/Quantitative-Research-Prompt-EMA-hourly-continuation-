# EMA Hourly Continuation — THETA/USDT P100_144

**Symbol:** THETA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.7172 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 0.9766 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -1.4994 |
| sortino_ratio | -0.3245 |
| max_drawdown | 0.3297 |
| cagr | -0.1378 |
| net_avg_win | 69.7744 |
| net_avg_loss | -96.4357 |
| avg_hold_time_bars | 5.1894 |
| exposure | 0.0535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
