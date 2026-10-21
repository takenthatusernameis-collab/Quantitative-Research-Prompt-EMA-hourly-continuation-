# EMA Hourly Continuation — FLUX/USDT P100_200

**Symbol:** FLUX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.8879 |
| net_win_rate | 0.5324 |
| gross_profit_factor | 1.1251 |
| gross_win_rate | 0.5324 |
| sharpe_ratio | -0.5594 |
| sortino_ratio | -0.1347 |
| max_drawdown | 0.1762 |
| cagr | -0.0626 |
| net_avg_win | 80.1967 |
| net_avg_loss | -102.8283 |
| avg_hold_time_bars | 12.2734 |
| exposure | 0.1551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
