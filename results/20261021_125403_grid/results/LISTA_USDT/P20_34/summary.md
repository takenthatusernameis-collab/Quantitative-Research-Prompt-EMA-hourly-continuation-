# EMA Hourly Continuation — LISTA/USDT P20_34

**Symbol:** LISTA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.6880 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9591 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -2.8191 |
| sortino_ratio | -0.8662 |
| max_drawdown | 0.6313 |
| cagr | -0.3290 |
| net_avg_win | 64.5477 |
| net_avg_loss | -86.7002 |
| avg_hold_time_bars | 5.6032 |
| exposure | 0.1181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
