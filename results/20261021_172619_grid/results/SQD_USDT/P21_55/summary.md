# EMA Hourly Continuation — SQD/USDT P21_55

**Symbol:** SQD/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.8569 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0503 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -1.1673 |
| sortino_ratio | -0.3858 |
| max_drawdown | 0.4213 |
| cagr | -0.1651 |
| net_avg_win | 81.1171 |
| net_avg_loss | -99.2046 |
| avg_hold_time_bars | 8.2070 |
| exposure | 0.1975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
