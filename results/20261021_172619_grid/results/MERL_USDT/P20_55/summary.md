# EMA Hourly Continuation — MERL/USDT P20_55

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.7697 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9361 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -1.8981 |
| sortino_ratio | -0.6074 |
| max_drawdown | 0.5552 |
| cagr | -0.2445 |
| net_avg_win | 69.6783 |
| net_avg_loss | -84.2547 |
| avg_hold_time_bars | 10.3725 |
| exposure | 0.2373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
