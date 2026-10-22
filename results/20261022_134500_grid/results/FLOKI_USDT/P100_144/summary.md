# EMA Hourly Continuation — FLOKI/USDT P100_144

**Symbol:** FLOKI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.4910 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.8768 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -4.9583 |
| sortino_ratio | -1.5286 |
| max_drawdown | 0.8570 |
| cagr | -0.5342 |
| net_avg_win | 37.2415 |
| net_avg_loss | -63.7344 |
| avg_hold_time_bars | 4.4566 |
| exposure | 0.0980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
