# EMA Hourly Continuation — SAFE/USDT P34_55

**Symbol:** SAFE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 842 |
| net_profit_factor | 0.4359 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.8951 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -7.2075 |
| sortino_ratio | -2.9521 |
| max_drawdown | 0.9757 |
| cagr | -0.7711 |
| net_avg_win | 19.7164 |
| net_avg_loss | -37.5615 |
| avg_hold_time_bars | 4.1698 |
| exposure | 0.1608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
