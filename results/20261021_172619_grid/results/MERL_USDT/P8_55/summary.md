# EMA Hourly Continuation — MERL/USDT P8_55

**Symbol:** MERL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.8282 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9715 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.4914 |
| sortino_ratio | -0.5568 |
| max_drawdown | 0.5483 |
| cagr | -0.2295 |
| net_avg_win | 68.6005 |
| net_avg_loss | -81.3791 |
| avg_hold_time_bars | 15.3118 |
| exposure | 0.4746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
