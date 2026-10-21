# EMA Hourly Continuation — KAVA/USDT P21_55

**Symbol:** KAVA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.6730 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9994 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -3.6047 |
| sortino_ratio | -1.2437 |
| max_drawdown | 0.7748 |
| cagr | -0.4398 |
| net_avg_win | 56.1569 |
| net_avg_loss | -77.6359 |
| avg_hold_time_bars | 8.3465 |
| exposure | 0.2212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
