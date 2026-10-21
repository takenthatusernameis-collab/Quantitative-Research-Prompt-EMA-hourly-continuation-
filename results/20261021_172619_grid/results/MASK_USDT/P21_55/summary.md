# EMA Hourly Continuation — MASK/USDT P21_55

**Symbol:** MASK/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.6620 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9607 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -3.1368 |
| sortino_ratio | -1.1000 |
| max_drawdown | 0.7308 |
| cagr | -0.3971 |
| net_avg_win | 47.9152 |
| net_avg_loss | -69.5462 |
| avg_hold_time_bars | 7.9817 |
| exposure | 0.2177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
