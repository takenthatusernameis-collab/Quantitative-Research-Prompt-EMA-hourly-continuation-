# EMA Hourly Continuation — MEME/USDT P21_55

**Symbol:** MEME/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1007 |
| net_profit_factor | 0.5503 |
| net_win_rate | 0.4518 |
| gross_profit_factor | 0.9108 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -6.5726 |
| sortino_ratio | -2.9305 |
| max_drawdown | 0.9742 |
| cagr | -0.7574 |
| net_avg_win | 26.1300 |
| net_avg_loss | -39.1375 |
| avg_hold_time_bars | 4.8550 |
| exposure | 0.2222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
