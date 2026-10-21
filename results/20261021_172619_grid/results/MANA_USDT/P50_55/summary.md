# EMA Hourly Continuation — MANA/USDT P50_55

**Symbol:** MANA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 121 |
| net_profit_factor | 0.5799 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8471 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -1.8987 |
| sortino_ratio | -0.2991 |
| max_drawdown | 0.3145 |
| cagr | -0.1280 |
| net_avg_win | 73.0587 |
| net_avg_loss | -104.9834 |
| avg_hold_time_bars | 5.0165 |
| exposure | 0.0276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
