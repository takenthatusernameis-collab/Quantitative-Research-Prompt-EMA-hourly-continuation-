# EMA Hourly Continuation — MINA/USDT P26_100

**Symbol:** MINA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.9108 |
| net_win_rate | 0.5394 |
| gross_profit_factor | 1.1532 |
| gross_win_rate | 0.5394 |
| sharpe_ratio | -0.5472 |
| sortino_ratio | -0.1713 |
| max_drawdown | 0.3612 |
| cagr | -0.0810 |
| net_avg_win | 77.1222 |
| net_avg_loss | -99.1846 |
| avg_hold_time_bars | 17.8635 |
| exposure | 0.3808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
