# EMA Hourly Continuation — FLOW/USDT P12_26

**Symbol:** FLOW/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1436 |
| net_profit_factor | 0.3298 |
| net_win_rate | 0.4060 |
| gross_profit_factor | 0.7834 |
| gross_win_rate | 0.4325 |
| sharpe_ratio | -12.4750 |
| sortino_ratio | -6.7336 |
| max_drawdown | 0.9998 |
| cagr | -0.9662 |
| net_avg_win | 8.4388 |
| net_avg_loss | -17.4886 |
| avg_hold_time_bars | 3.0543 |
| exposure | 0.1994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
