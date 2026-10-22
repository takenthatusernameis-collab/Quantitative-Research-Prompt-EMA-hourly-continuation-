# EMA Hourly Continuation — VR/USDT P50_89

**Symbol:** VR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.5220 |
| net_win_rate | 0.4142 |
| gross_profit_factor | 0.7347 |
| gross_win_rate | 0.4184 |
| sharpe_ratio | -3.2098 |
| sortino_ratio | -0.7026 |
| max_drawdown | 0.5597 |
| cagr | -0.2787 |
| net_avg_win | 61.7500 |
| net_avg_loss | -83.6482 |
| avg_hold_time_bars | 9.2343 |
| exposure | 0.1003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
