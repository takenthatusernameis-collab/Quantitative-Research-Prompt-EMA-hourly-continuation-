# EMA Hourly Continuation — KSM/USDT P8_12

**Symbol:** KSM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.5476 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.8373 |
| gross_win_rate | 0.4399 |
| sharpe_ratio | -3.8129 |
| sortino_ratio | -1.0097 |
| max_drawdown | 0.6961 |
| cagr | -0.3709 |
| net_avg_win | 55.4946 |
| net_avg_loss | -79.5881 |
| avg_hold_time_bars | 4.3959 |
| exposure | 0.0681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
