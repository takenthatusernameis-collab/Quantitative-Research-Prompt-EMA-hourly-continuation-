# EMA Hourly Continuation — DOGS/USDT P26_144

**Symbol:** DOGS/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.7214 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 0.9846 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -2.3334 |
| sortino_ratio | -0.7243 |
| max_drawdown | 0.5510 |
| cagr | -0.2910 |
| net_avg_win | 65.7194 |
| net_avg_loss | -89.7961 |
| avg_hold_time_bars | 23.1181 |
| exposure | 0.5090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
