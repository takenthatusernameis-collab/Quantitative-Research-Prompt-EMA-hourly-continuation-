# EMA Hourly Continuation — FLIP/USDT P89_100

**Symbol:** FLIP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.2836 |
| net_win_rate | 0.3265 |
| gross_profit_factor | 0.8070 |
| gross_win_rate | 0.4062 |
| sharpe_ratio | -8.3397 |
| sortino_ratio | -2.4050 |
| max_drawdown | 0.9586 |
| cagr | -0.7157 |
| net_avg_win | 29.8531 |
| net_avg_loss | -51.0174 |
| avg_hold_time_bars | 5.7121 |
| exposure | 0.1010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
