# EMA Hourly Continuation — AGLD/USDT P20_144

**Symbol:** AGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.7372 |
| net_win_rate | 0.4895 |
| gross_profit_factor | 1.0031 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -2.5369 |
| sortino_ratio | -0.8134 |
| max_drawdown | 0.6614 |
| cagr | -0.3215 |
| net_avg_win | 68.3922 |
| net_avg_loss | -88.9498 |
| avg_hold_time_bars | 23.2390 |
| exposure | 0.5500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
