# EMA Hourly Continuation — ATOM/USDT P100_144

**Symbol:** ATOM/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.6803 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9737 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.6951 |
| sortino_ratio | -0.3532 |
| max_drawdown | 0.3327 |
| cagr | -0.1488 |
| net_avg_win | 68.0647 |
| net_avg_loss | -98.1635 |
| avg_hold_time_bars | 6.0905 |
| exposure | 0.0581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
