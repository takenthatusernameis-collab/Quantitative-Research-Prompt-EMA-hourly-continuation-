# EMA Hourly Continuation — DEXE/USDT P21_89

**Symbol:** DEXE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.6128 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9412 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -3.3722 |
| sortino_ratio | -1.1437 |
| max_drawdown | 0.7492 |
| cagr | -0.4218 |
| net_avg_win | 42.2461 |
| net_avg_loss | -63.7060 |
| avg_hold_time_bars | 19.7101 |
| exposure | 0.5223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
