# EMA Hourly Continuation — BAND/USDT P89_100

**Symbol:** BAND/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 183 |
| net_profit_factor | 0.4724 |
| net_win_rate | 0.4262 |
| gross_profit_factor | 0.7799 |
| gross_win_rate | 0.4372 |
| sharpe_ratio | -3.1536 |
| sortino_ratio | -0.6110 |
| max_drawdown | 0.5189 |
| cagr | -0.2466 |
| net_avg_win | 58.6109 |
| net_avg_loss | -92.1615 |
| avg_hold_time_bars | 4.5464 |
| exposure | 0.0376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
