# EMA Hourly Continuation — DEEP/USDT P34_89

**Symbol:** DEEP/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.8020 |
| net_win_rate | 0.5212 |
| gross_profit_factor | 1.1091 |
| gross_win_rate | 0.5212 |
| sharpe_ratio | -1.9552 |
| sortino_ratio | -0.6912 |
| max_drawdown | 0.5217 |
| cagr | -0.2785 |
| net_avg_win | 75.7137 |
| net_avg_loss | -102.7700 |
| avg_hold_time_bars | 8.0747 |
| exposure | 0.2263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
