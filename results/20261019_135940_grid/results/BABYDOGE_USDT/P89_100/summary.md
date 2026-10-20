# EMA Hourly Continuation — BABYDOGE/USDT P89_100

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 8 |
| net_profit_factor | 1.4779 |
| net_win_rate | 0.6250 |
| gross_profit_factor | 1.6476 |
| gross_win_rate | 0.6250 |
| sharpe_ratio | 0.3503 |
| sortino_ratio | 0.0149 |
| max_drawdown | 0.0115 |
| cagr | 0.0061 |
| net_avg_win | 94.9609 |
| net_avg_loss | -107.0911 |
| avg_hold_time_bars | 18.2500 |
| exposure | 0.0066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
