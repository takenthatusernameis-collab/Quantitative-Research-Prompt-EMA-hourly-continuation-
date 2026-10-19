# EMA Hourly Continuation — ZBCN/USDT P20_55

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1063 |
| net_profit_factor | 0.5922 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9454 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -5.8825 |
| sortino_ratio | -2.7117 |
| max_drawdown | 0.9629 |
| cagr | -0.7329 |
| net_avg_win | 27.8746 |
| net_avg_loss | -41.9579 |
| avg_hold_time_bars | 4.3565 |
| exposure | 0.2143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
