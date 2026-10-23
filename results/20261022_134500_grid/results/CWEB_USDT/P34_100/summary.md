# EMA Hourly Continuation — CWEB/USDT P34_100

**Symbol:** CWEB/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.5329 |
| net_win_rate | 0.4235 |
| gross_profit_factor | 0.8750 |
| gross_win_rate | 0.4275 |
| sharpe_ratio | -5.8045 |
| sortino_ratio | -1.8393 |
| max_drawdown | 0.9082 |
| cagr | -0.6042 |
| net_avg_win | 47.6697 |
| net_avg_loss | -65.7190 |
| avg_hold_time_bars | 14.8216 |
| exposure | 0.3436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
