# EMA Hourly Continuation — RENDER/USDT P21_200

**Symbol:** RENDER/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 1.0307 |
| net_win_rate | 0.5470 |
| gross_profit_factor | 1.1869 |
| gross_win_rate | 0.5470 |
| sharpe_ratio | 0.2085 |
| sortino_ratio | 0.0498 |
| max_drawdown | 0.1137 |
| cagr | 0.0164 |
| net_avg_win | 93.8628 |
| net_avg_loss | -109.9667 |
| avg_hold_time_bars | 51.1923 |
| exposure | 0.6322 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
