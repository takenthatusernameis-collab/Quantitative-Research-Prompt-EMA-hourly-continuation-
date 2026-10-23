# EMA Hourly Continuation — PROM/USDT P8_144

**Symbol:** PROM/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.4768 |
| net_win_rate | 0.4081 |
| gross_profit_factor | 0.7286 |
| gross_win_rate | 0.4252 |
| sharpe_ratio | -5.9559 |
| sortino_ratio | -2.1111 |
| max_drawdown | 0.9246 |
| cagr | -0.6401 |
| net_avg_win | 32.1107 |
| net_avg_loss | -46.4336 |
| avg_hold_time_bars | 23.2819 |
| exposure | 0.6794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
