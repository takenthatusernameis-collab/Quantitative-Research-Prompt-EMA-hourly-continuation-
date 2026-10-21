# EMA Hourly Continuation — MINA/USDT P8_26

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 778 |
| net_profit_factor | 0.7549 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0423 |
| gross_win_rate | 0.5129 |
| sharpe_ratio | -2.4585 |
| sortino_ratio | -0.9858 |
| max_drawdown | 0.7180 |
| cagr | -0.3635 |
| net_avg_win | 52.3584 |
| net_avg_loss | -73.0229 |
| avg_hold_time_bars | 6.6452 |
| exposure | 0.2350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
