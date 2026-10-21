# EMA Hourly Continuation — ORBS/USDT P89_100

**Symbol:** ORBS/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 192 |
| net_profit_factor | 0.4581 |
| net_win_rate | 0.4219 |
| gross_profit_factor | 0.7786 |
| gross_win_rate | 0.4219 |
| sharpe_ratio | -3.5590 |
| sortino_ratio | -0.7082 |
| max_drawdown | 0.5688 |
| cagr | -0.2825 |
| net_avg_win | 59.0308 |
| net_avg_loss | -94.0276 |
| avg_hold_time_bars | 5.9740 |
| exposure | 0.0521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
