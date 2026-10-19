# EMA Hourly Continuation — ETC/USDT P26_200

**Symbol:** ETC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.5937 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9470 |
| gross_win_rate | 0.4861 |
| sharpe_ratio | -3.2289 |
| sortino_ratio | -0.8550 |
| max_drawdown | 0.6659 |
| cagr | -0.3425 |
| net_avg_win | 55.6303 |
| net_avg_loss | -84.7810 |
| avg_hold_time_bars | 36.8000 |
| exposure | 0.6022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
