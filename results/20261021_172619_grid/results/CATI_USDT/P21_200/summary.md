# EMA Hourly Continuation — CATI/USDT P21_200

**Symbol:** CATI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.6330 |
| net_win_rate | 0.4387 |
| gross_profit_factor | 0.7737 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -2.5214 |
| sortino_ratio | -0.6219 |
| max_drawdown | 0.4995 |
| cagr | -0.2498 |
| net_avg_win | 69.9824 |
| net_avg_loss | -86.4240 |
| avg_hold_time_bars | 46.6285 |
| exposure | 0.6467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
