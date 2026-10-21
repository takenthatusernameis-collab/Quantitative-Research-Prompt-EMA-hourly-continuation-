# EMA Hourly Continuation — TRAC/USDT P21_55

**Symbol:** TRAC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.7920 |
| net_win_rate | 0.5122 |
| gross_profit_factor | 1.0401 |
| gross_win_rate | 0.5122 |
| sharpe_ratio | -1.5485 |
| sortino_ratio | -0.4937 |
| max_drawdown | 0.4761 |
| cagr | -0.2028 |
| net_avg_win | 65.5865 |
| net_avg_loss | -86.9521 |
| avg_hold_time_bars | 9.9736 |
| exposure | 0.2230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
