# EMA Hourly Continuation — SAND/USDT P34_55

**Symbol:** SAND/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.6402 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9228 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.4905 |
| sortino_ratio | -0.6191 |
| max_drawdown | 0.5479 |
| cagr | -0.2456 |
| net_avg_win | 63.1284 |
| net_avg_loss | -89.2398 |
| avg_hold_time_bars | 5.8040 |
| exposure | 0.0794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
