# EMA Hourly Continuation — AIOZ/USDT P26_50

**Symbol:** AIOZ/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1035 |
| net_profit_factor | 0.5360 |
| net_win_rate | 0.4396 |
| gross_profit_factor | 0.9010 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -8.1461 |
| sortino_ratio | -3.6830 |
| max_drawdown | 0.9903 |
| cagr | -0.8403 |
| net_avg_win | 25.1350 |
| net_avg_loss | -36.7872 |
| avg_hold_time_bars | 3.7053 |
| exposure | 0.1743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
