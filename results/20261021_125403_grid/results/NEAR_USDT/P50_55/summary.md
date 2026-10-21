# EMA Hourly Continuation — NEAR/USDT P50_55

**Symbol:** NEAR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 79 |
| net_profit_factor | 0.6937 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9183 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -0.9892 |
| sortino_ratio | -0.1258 |
| max_drawdown | 0.1413 |
| cagr | -0.0560 |
| net_avg_win | 80.3209 |
| net_avg_loss | -107.3194 |
| avg_hold_time_bars | 5.3418 |
| exposure | 0.0192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
