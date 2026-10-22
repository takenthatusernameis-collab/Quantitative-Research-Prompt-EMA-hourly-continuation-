# EMA Hourly Continuation — SATS/USDT P50_55

**Symbol:** SATS/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 138 |
| net_profit_factor | 0.5180 |
| net_win_rate | 0.4275 |
| gross_profit_factor | 0.7413 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -2.2233 |
| sortino_ratio | -0.3711 |
| max_drawdown | 0.3575 |
| cagr | -0.1560 |
| net_avg_win | 63.3966 |
| net_avg_loss | -91.4109 |
| avg_hold_time_bars | 5.4348 |
| exposure | 0.0339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
