# EMA Hourly Continuation — CRV/USDT P12_20

**Symbol:** CRV/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.7419 |
| net_win_rate | 0.5112 |
| gross_profit_factor | 1.0176 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -1.3820 |
| sortino_ratio | -0.3256 |
| max_drawdown | 0.3477 |
| cagr | -0.1383 |
| net_avg_win | 65.4539 |
| net_avg_loss | -92.2601 |
| avg_hold_time_bars | 4.5448 |
| exposure | 0.0554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
