# EMA Hourly Continuation — TRX/USDT P55_144

**Symbol:** TRX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.3348 |
| net_win_rate | 0.4240 |
| gross_profit_factor | 1.0500 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -7.0750 |
| sortino_ratio | -2.1165 |
| max_drawdown | 0.9397 |
| cagr | -0.6714 |
| net_avg_win | 25.2652 |
| net_avg_loss | -55.5651 |
| avg_hold_time_bars | 11.3560 |
| exposure | 0.2276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
