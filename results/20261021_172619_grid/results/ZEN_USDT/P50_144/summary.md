# EMA Hourly Continuation — ZEN/USDT P50_144

**Symbol:** ZEN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.7203 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9039 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -2.0794 |
| sortino_ratio | -0.5811 |
| max_drawdown | 0.5103 |
| cagr | -0.2357 |
| net_avg_win | 69.4416 |
| net_avg_loss | -86.4378 |
| avg_hold_time_bars | 15.4519 |
| exposure | 0.2704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
