# EMA Hourly Continuation — CARV/USDT P89_100

**Symbol:** CARV/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 118 |
| net_profit_factor | 0.3513 |
| net_win_rate | 0.3729 |
| gross_profit_factor | 0.5673 |
| gross_win_rate | 0.3729 |
| sharpe_ratio | -3.5773 |
| sortino_ratio | -0.6187 |
| max_drawdown | 0.4604 |
| cagr | -0.2502 |
| net_avg_win | 54.4417 |
| net_avg_loss | -92.1546 |
| avg_hold_time_bars | 5.3305 |
| exposure | 0.0354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
