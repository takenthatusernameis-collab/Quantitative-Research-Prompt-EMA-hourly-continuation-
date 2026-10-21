# EMA Hourly Continuation — POPCAT/USDT P8_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.9623 |
| net_win_rate | 0.5284 |
| gross_profit_factor | 1.1105 |
| gross_win_rate | 0.5284 |
| sharpe_ratio | -0.1992 |
| sortino_ratio | -0.0610 |
| max_drawdown | 0.2666 |
| cagr | -0.0350 |
| net_avg_win | 92.3567 |
| net_avg_loss | -107.5131 |
| avg_hold_time_bars | 32.4278 |
| exposure | 0.6647 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
