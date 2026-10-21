# EMA Hourly Continuation — IOST/USDT P50_100

**Symbol:** IOST/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.7452 |
| net_win_rate | 0.5147 |
| gross_profit_factor | 1.0816 |
| gross_win_rate | 0.5147 |
| sharpe_ratio | -2.0188 |
| sortino_ratio | -0.5866 |
| max_drawdown | 0.5192 |
| cagr | -0.2364 |
| net_avg_win | 68.5096 |
| net_avg_loss | -97.5108 |
| avg_hold_time_bars | 9.5221 |
| exposure | 0.1766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
