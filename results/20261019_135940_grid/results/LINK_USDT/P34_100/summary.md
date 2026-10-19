# EMA Hourly Continuation — LINK/USDT P34_100

**Symbol:** LINK/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.5656 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.9517 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -5.0606 |
| sortino_ratio | -1.7255 |
| max_drawdown | 0.8893 |
| cagr | -0.5775 |
| net_avg_win | 41.6015 |
| net_avg_loss | -63.2750 |
| avg_hold_time_bars | 9.6394 |
| exposure | 0.2625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
