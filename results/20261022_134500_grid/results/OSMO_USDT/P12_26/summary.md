# EMA Hourly Continuation — OSMO/USDT P12_26

**Symbol:** OSMO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1391 |
| net_profit_factor | 0.4682 |
| net_win_rate | 0.4069 |
| gross_profit_factor | 1.1748 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -12.0227 |
| sortino_ratio | -6.3937 |
| max_drawdown | 0.9997 |
| cagr | -0.9583 |
| net_avg_win | 15.5493 |
| net_avg_loss | -22.7848 |
| avg_hold_time_bars | 3.3422 |
| exposure | 0.2113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
