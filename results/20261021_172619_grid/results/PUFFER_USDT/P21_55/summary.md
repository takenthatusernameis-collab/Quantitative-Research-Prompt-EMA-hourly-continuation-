# EMA Hourly Continuation — PUFFER/USDT P21_55

**Symbol:** PUFFER/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.9660 |
| net_win_rate | 0.5495 |
| gross_profit_factor | 1.2092 |
| gross_win_rate | 0.5495 |
| sharpe_ratio | -0.1690 |
| sortino_ratio | -0.0550 |
| max_drawdown | 0.1489 |
| cagr | -0.0333 |
| net_avg_win | 84.6443 |
| net_avg_loss | -106.8804 |
| avg_hold_time_bars | 9.0520 |
| exposure | 0.2069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
