# EMA Hourly Continuation — CPOOL/USDT P20_55

**Symbol:** CPOOL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.7298 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.8778 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -2.0244 |
| sortino_ratio | -0.6420 |
| max_drawdown | 0.5411 |
| cagr | -0.2565 |
| net_avg_win | 60.0870 |
| net_avg_loss | -74.7294 |
| avg_hold_time_bars | 8.3871 |
| exposure | 0.1891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
