# EMA Hourly Continuation — XMR/USDT P8_12

**Symbol:** XMR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 118 |
| net_profit_factor | 0.6108 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8597 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -1.7172 |
| sortino_ratio | -0.2667 |
| max_drawdown | 0.2651 |
| cagr | -0.1154 |
| net_avg_win | 77.0602 |
| net_avg_loss | -106.4433 |
| avg_hold_time_bars | 4.6864 |
| exposure | 0.0251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
