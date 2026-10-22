# EMA Hourly Continuation — PEOPLE/USDT P20_50

**Symbol:** PEOPLE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.7161 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9219 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -2.6758 |
| sortino_ratio | -0.8963 |
| max_drawdown | 0.6541 |
| cagr | -0.3368 |
| net_avg_win | 61.6382 |
| net_avg_loss | -78.6278 |
| avg_hold_time_bars | 7.2712 |
| exposure | 0.1820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
