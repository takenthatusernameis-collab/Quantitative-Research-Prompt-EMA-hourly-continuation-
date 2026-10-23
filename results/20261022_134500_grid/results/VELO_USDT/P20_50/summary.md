# EMA Hourly Continuation — VELO/USDT P20_50

**Symbol:** VELO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1073 |
| net_profit_factor | 0.5447 |
| net_win_rate | 0.4567 |
| gross_profit_factor | 0.8239 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -6.2015 |
| sortino_ratio | -2.8607 |
| max_drawdown | 0.9703 |
| cagr | -0.7453 |
| net_avg_win | 23.6292 |
| net_avg_loss | -36.4598 |
| avg_hold_time_bars | 4.2824 |
| exposure | 0.2089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
