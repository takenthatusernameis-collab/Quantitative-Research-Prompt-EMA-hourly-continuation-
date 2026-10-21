# EMA Hourly Continuation — JASMY/USDT P34_55

**Symbol:** JASMY/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.6732 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.8973 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -1.9850 |
| sortino_ratio | -0.4635 |
| max_drawdown | 0.4131 |
| cagr | -0.1911 |
| net_avg_win | 66.9768 |
| net_avg_loss | -90.2521 |
| avg_hold_time_bars | 5.1648 |
| exposure | 0.0627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
