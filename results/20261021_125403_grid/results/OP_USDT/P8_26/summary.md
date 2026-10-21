# EMA Hourly Continuation — OP/USDT P8_26

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.8345 |
| net_win_rate | 0.5277 |
| gross_profit_factor | 1.1038 |
| gross_win_rate | 0.5277 |
| sharpe_ratio | -1.3759 |
| sortino_ratio | -0.5062 |
| max_drawdown | 0.5478 |
| cagr | -0.2101 |
| net_avg_win | 65.6904 |
| net_avg_loss | -87.9499 |
| avg_hold_time_bars | 6.9677 |
| exposure | 0.2059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
