# EMA Hourly Continuation — LINK/USDT P50_55

**Symbol:** LINK/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 89 |
| net_profit_factor | 0.8251 |
| net_win_rate | 0.5393 |
| gross_profit_factor | 1.1579 |
| gross_win_rate | 0.5393 |
| sharpe_ratio | -0.5324 |
| sortino_ratio | -0.0727 |
| max_drawdown | 0.1060 |
| cagr | -0.0331 |
| net_avg_win | 79.6834 |
| net_avg_loss | -113.0660 |
| avg_hold_time_bars | 6.1910 |
| exposure | 0.0250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
