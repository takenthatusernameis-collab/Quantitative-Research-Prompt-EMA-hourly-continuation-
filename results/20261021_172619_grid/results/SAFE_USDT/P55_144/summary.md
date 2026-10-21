# EMA Hourly Continuation — SAFE/USDT P55_144

**Symbol:** SAFE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.8061 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0060 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.2516 |
| sortino_ratio | -0.3305 |
| max_drawdown | 0.3584 |
| cagr | -0.1419 |
| net_avg_win | 78.0133 |
| net_avg_loss | -97.3538 |
| avg_hold_time_bars | 17.7122 |
| exposure | 0.2734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
