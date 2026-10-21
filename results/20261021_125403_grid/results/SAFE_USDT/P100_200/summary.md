# EMA Hourly Continuation — SAFE/USDT P100_200

**Symbol:** SAFE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.7565 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9735 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -1.4470 |
| sortino_ratio | -0.3388 |
| max_drawdown | 0.3382 |
| cagr | -0.1444 |
| net_avg_win | 76.3692 |
| net_avg_loss | -97.9640 |
| avg_hold_time_bars | 13.3797 |
| exposure | 0.1630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
