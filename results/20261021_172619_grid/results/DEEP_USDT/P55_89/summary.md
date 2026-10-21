# EMA Hourly Continuation — DEEP/USDT P55_89

**Symbol:** DEEP/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.9953 |
| net_win_rate | 0.5633 |
| gross_profit_factor | 1.2778 |
| gross_win_rate | 0.5633 |
| sharpe_ratio | 0.0284 |
| sortino_ratio | 0.0072 |
| max_drawdown | 0.1451 |
| cagr | -0.0029 |
| net_avg_win | 90.8734 |
| net_avg_loss | -117.7541 |
| avg_hold_time_bars | 6.1551 |
| exposure | 0.0854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
