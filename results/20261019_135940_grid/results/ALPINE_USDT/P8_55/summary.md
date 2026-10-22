# EMA Hourly Continuation — ALPINE/USDT P8_55

**Symbol:** ALPINE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 943 |
| net_profit_factor | 0.4849 |
| net_win_rate | 0.4263 |
| gross_profit_factor | 0.7739 |
| gross_win_rate | 0.4496 |
| sharpe_ratio | -6.8219 |
| sortino_ratio | -2.9336 |
| max_drawdown | 0.9736 |
| cagr | -0.7604 |
| net_avg_win | 22.7693 |
| net_avg_loss | -34.8922 |
| avg_hold_time_bars | 10.9799 |
| exposure | 0.4706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
