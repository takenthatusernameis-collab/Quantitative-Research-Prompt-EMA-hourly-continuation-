# EMA Hourly Continuation — REZ/USDT P89_100

**Symbol:** REZ/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.3700 |
| net_win_rate | 0.4085 |
| gross_profit_factor | 0.7506 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -7.7053 |
| sortino_ratio | -2.7416 |
| max_drawdown | 0.9654 |
| cagr | -0.7432 |
| net_avg_win | 22.6765 |
| net_avg_loss | -42.3292 |
| avg_hold_time_bars | 2.5359 |
| exposure | 0.0716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
