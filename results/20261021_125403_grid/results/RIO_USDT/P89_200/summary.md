# EMA Hourly Continuation — RIO/USDT P89_200

**Symbol:** RIO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.7036 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.8132 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -1.9141 |
| sortino_ratio | -0.4553 |
| max_drawdown | 0.4458 |
| cagr | -0.1901 |
| net_avg_win | 77.4510 |
| net_avg_loss | -88.7786 |
| avg_hold_time_bars | 13.5571 |
| exposure | 0.1743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
