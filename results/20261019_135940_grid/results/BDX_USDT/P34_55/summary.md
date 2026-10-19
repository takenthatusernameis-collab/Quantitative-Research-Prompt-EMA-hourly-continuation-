# EMA Hourly Continuation — BDX/USDT P34_55

**Symbol:** BDX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1341 |
| net_profit_factor | 0.1893 |
| net_win_rate | 0.2140 |
| gross_profit_factor | 0.6321 |
| gross_win_rate | 0.3117 |
| sharpe_ratio | -22.0145 |
| sortino_ratio | -12.9156 |
| max_drawdown | 1.0000 |
| cagr | -0.9993 |
| net_avg_win | 8.1358 |
| net_avg_loss | -11.7030 |
| avg_hold_time_bars | 2.3244 |
| exposure | 0.1417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
