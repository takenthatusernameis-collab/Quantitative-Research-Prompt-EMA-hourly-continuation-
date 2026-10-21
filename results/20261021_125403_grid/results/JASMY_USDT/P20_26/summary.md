# EMA Hourly Continuation — JASMY/USDT P20_26

**Symbol:** JASMY/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 121 |
| net_profit_factor | 0.6552 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.8768 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -1.4094 |
| sortino_ratio | -0.2216 |
| max_drawdown | 0.2474 |
| cagr | -0.0966 |
| net_avg_win | 75.0902 |
| net_avg_loss | -102.0736 |
| avg_hold_time_bars | 3.9835 |
| exposure | 0.0219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
