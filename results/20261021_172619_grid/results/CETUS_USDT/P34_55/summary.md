# EMA Hourly Continuation — CETUS/USDT P34_55

**Symbol:** CETUS/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6541 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.8859 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -2.4366 |
| sortino_ratio | -0.6634 |
| max_drawdown | 0.5458 |
| cagr | -0.2620 |
| net_avg_win | 58.5003 |
| net_avg_loss | -80.5913 |
| avg_hold_time_bars | 5.4137 |
| exposure | 0.0894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
