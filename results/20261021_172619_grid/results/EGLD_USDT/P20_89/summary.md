# EMA Hourly Continuation — EGLD/USDT P20_89

**Symbol:** EGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.8379 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0812 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -1.2834 |
| sortino_ratio | -0.4233 |
| max_drawdown | 0.4616 |
| cagr | -0.1787 |
| net_avg_win | 73.8657 |
| net_avg_loss | -95.5004 |
| avg_hold_time_bars | 16.0686 |
| exposure | 0.3835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
