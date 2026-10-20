# EMA Hourly Continuation — ORCA/USDT P8_144

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.6464 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.9099 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -2.9790 |
| sortino_ratio | -0.9076 |
| max_drawdown | 0.6832 |
| cagr | -0.3555 |
| net_avg_win | 54.2799 |
| net_avg_loss | -74.9797 |
| avg_hold_time_bars | 34.3124 |
| exposure | 0.7440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
