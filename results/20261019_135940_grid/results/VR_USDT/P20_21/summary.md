# EMA Hourly Continuation — VR/USDT P20_21

**Symbol:** VR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1316 |
| net_profit_factor | 0.1626 |
| net_win_rate | 0.2059 |
| gross_profit_factor | 0.4850 |
| gross_win_rate | 0.2523 |
| sharpe_ratio | -22.8603 |
| sortino_ratio | -13.7747 |
| max_drawdown | 1.0000 |
| cagr | -0.9997 |
| net_avg_win | 7.1631 |
| net_avg_loss | -11.4270 |
| avg_hold_time_bars | 1.9316 |
| exposure | 0.1155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
