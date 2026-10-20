# EMA Hourly Continuation — CPOOL/USDT P50_100

**Symbol:** CPOOL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.5800 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.8548 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -5.1586 |
| sortino_ratio | -1.9056 |
| max_drawdown | 0.9096 |
| cagr | -0.6051 |
| net_avg_win | 39.4654 |
| net_avg_loss | -56.4334 |
| avg_hold_time_bars | 4.5323 |
| exposure | 0.1436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
