# EMA Hourly Continuation — CTSI/USDT P50_89

**Symbol:** CTSI/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.6248 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.8810 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -3.1385 |
| sortino_ratio | -0.9590 |
| max_drawdown | 0.6712 |
| cagr | -0.3555 |
| net_avg_win | 51.7401 |
| net_avg_loss | -73.5772 |
| avg_hold_time_bars | 7.3676 |
| exposure | 0.1530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
