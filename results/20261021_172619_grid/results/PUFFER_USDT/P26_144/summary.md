# EMA Hourly Continuation — PUFFER/USDT P26_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.9697 |
| net_win_rate | 0.5336 |
| gross_profit_factor | 1.1359 |
| gross_win_rate | 0.5336 |
| sharpe_ratio | -0.1179 |
| sortino_ratio | -0.0328 |
| max_drawdown | 0.1692 |
| cagr | -0.0216 |
| net_avg_win | 86.4584 |
| net_avg_loss | -101.9938 |
| avg_hold_time_bars | 28.9329 |
| exposure | 0.4879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
