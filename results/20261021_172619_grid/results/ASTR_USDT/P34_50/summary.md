# EMA Hourly Continuation — ASTR/USDT P34_50

**Symbol:** ASTR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.6321 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0180 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -2.8006 |
| sortino_ratio | -0.7513 |
| max_drawdown | 0.5877 |
| cagr | -0.2929 |
| net_avg_win | 57.2270 |
| net_avg_loss | -90.5310 |
| avg_hold_time_bars | 5.6829 |
| exposure | 0.0900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
