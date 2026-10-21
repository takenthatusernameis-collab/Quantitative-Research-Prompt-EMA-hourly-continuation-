# EMA Hourly Continuation — VELO/USDT P8_20

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.9075 |
| net_win_rate | 0.5416 |
| gross_profit_factor | 1.1765 |
| gross_win_rate | 0.5416 |
| sharpe_ratio | -0.6388 |
| sortino_ratio | -0.1952 |
| max_drawdown | 0.3396 |
| cagr | -0.0896 |
| net_avg_win | 85.4498 |
| net_avg_loss | -111.2418 |
| avg_hold_time_bars | 5.5326 |
| exposure | 0.1119 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
