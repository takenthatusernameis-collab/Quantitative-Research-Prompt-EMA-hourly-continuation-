# EMA Hourly Continuation — PUFFER/USDT P55_100

**Symbol:** PUFFER/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.7327 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 0.9271 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -1.8456 |
| sortino_ratio | -0.5077 |
| max_drawdown | 0.4156 |
| cagr | -0.2077 |
| net_avg_win | 71.3252 |
| net_avg_loss | -91.0295 |
| avg_hold_time_bars | 9.6611 |
| exposure | 0.1629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
