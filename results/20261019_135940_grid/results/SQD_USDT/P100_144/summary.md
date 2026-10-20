# EMA Hourly Continuation — SQD/USDT P100_144

**Symbol:** SQD/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.5762 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.9202 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -3.7336 |
| sortino_ratio | -1.1562 |
| max_drawdown | 0.7428 |
| cagr | -0.4235 |
| net_avg_win | 45.5741 |
| net_avg_loss | -70.4531 |
| avg_hold_time_bars | 4.6274 |
| exposure | 0.1016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
