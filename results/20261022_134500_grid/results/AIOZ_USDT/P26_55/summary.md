# EMA Hourly Continuation — AIOZ/USDT P26_55

**Symbol:** AIOZ/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1002 |
| net_profit_factor | 0.5796 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.9317 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -7.5334 |
| sortino_ratio | -3.3587 |
| max_drawdown | 0.9846 |
| cagr | -0.8077 |
| net_avg_win | 30.5531 |
| net_avg_loss | -41.9469 |
| avg_hold_time_bars | 4.2136 |
| exposure | 0.1919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
