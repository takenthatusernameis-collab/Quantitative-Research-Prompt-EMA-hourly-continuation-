# EMA Hourly Continuation — POPCAT/USDT P20_34

**Symbol:** POPCAT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.6544 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.8417 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -2.6986 |
| sortino_ratio | -0.7312 |
| max_drawdown | 0.5442 |
| cagr | -0.2855 |
| net_avg_win | 68.8620 |
| net_avg_loss | -87.8979 |
| avg_hold_time_bars | 5.2596 |
| exposure | 0.0867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
