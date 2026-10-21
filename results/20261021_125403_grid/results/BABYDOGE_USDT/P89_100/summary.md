# EMA Hourly Continuation — BABYDOGE/USDT P89_100

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 6 |
| net_profit_factor | 0.9059 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9910 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.0693 |
| sortino_ratio | -0.0024 |
| max_drawdown | 0.0213 |
| cagr | -0.0012 |
| net_avg_win | 96.4304 |
| net_avg_loss | -106.4503 |
| avg_hold_time_bars | 23.5000 |
| exposure | 0.0064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
