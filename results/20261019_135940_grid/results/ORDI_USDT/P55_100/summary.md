# EMA Hourly Continuation — ORDI/USDT P55_100

**Symbol:** ORDI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.6529 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 1.0570 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -3.5601 |
| sortino_ratio | -1.2580 |
| max_drawdown | 0.7692 |
| cagr | -0.4413 |
| net_avg_win | 47.3685 |
| net_avg_loss | -71.8495 |
| avg_hold_time_bars | 5.1697 |
| exposure | 0.1440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
