# EMA Hourly Continuation — POLYX/USDT P50_89

**Symbol:** POLYX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.6826 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9730 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -2.6121 |
| sortino_ratio | -0.7636 |
| max_drawdown | 0.5975 |
| cagr | -0.2942 |
| net_avg_win | 61.7747 |
| net_avg_loss | -86.2527 |
| avg_hold_time_bars | 7.3149 |
| exposure | 0.1383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
