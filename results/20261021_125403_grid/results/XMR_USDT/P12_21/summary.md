# EMA Hourly Continuation — XMR/USDT P12_21

**Symbol:** XMR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 180 |
| net_profit_factor | 0.5857 |
| net_win_rate | 0.4556 |
| gross_profit_factor | 0.8344 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -2.1856 |
| sortino_ratio | -0.4192 |
| max_drawdown | 0.3897 |
| cagr | -0.1746 |
| net_avg_win | 65.9330 |
| net_avg_loss | -94.1873 |
| avg_hold_time_bars | 4.5111 |
| exposure | 0.0369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
