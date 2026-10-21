# EMA Hourly Continuation — SATS/USDT P34_55

**Symbol:** SATS/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.5257 |
| net_win_rate | 0.4252 |
| gross_profit_factor | 0.7374 |
| gross_win_rate | 0.4282 |
| sharpe_ratio | -3.6308 |
| sortino_ratio | -0.9492 |
| max_drawdown | 0.6781 |
| cagr | -0.3577 |
| net_avg_win | 51.4192 |
| net_avg_loss | -72.3602 |
| avg_hold_time_bars | 5.4545 |
| exposure | 0.0842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
