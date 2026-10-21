# EMA Hourly Continuation — CYBER/USDT P20_55

**Symbol:** CYBER/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.6561 |
| net_win_rate | 0.4617 |
| gross_profit_factor | 0.8688 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -3.4579 |
| sortino_ratio | -1.2065 |
| max_drawdown | 0.7627 |
| cagr | -0.4259 |
| net_avg_win | 51.7875 |
| net_avg_loss | -67.6898 |
| avg_hold_time_bars | 9.3817 |
| exposure | 0.2559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
