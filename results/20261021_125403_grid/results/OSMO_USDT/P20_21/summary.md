# EMA Hourly Continuation — OSMO/USDT P20_21

**Symbol:** OSMO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.4729 |
| net_win_rate | 0.3992 |
| gross_profit_factor | 0.7494 |
| gross_win_rate | 0.3992 |
| sharpe_ratio | -4.0746 |
| sortino_ratio | -0.9013 |
| max_drawdown | 0.6555 |
| cagr | -0.3426 |
| net_avg_win | 61.5050 |
| net_avg_loss | -86.4015 |
| avg_hold_time_bars | 4.7017 |
| exposure | 0.0509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
