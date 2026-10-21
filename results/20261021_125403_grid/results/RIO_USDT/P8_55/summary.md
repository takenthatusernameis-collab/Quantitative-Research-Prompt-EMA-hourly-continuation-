# EMA Hourly Continuation — RIO/USDT P8_55

**Symbol:** RIO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.8213 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9396 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -1.6864 |
| sortino_ratio | -0.6302 |
| max_drawdown | 0.5372 |
| cagr | -0.2548 |
| net_avg_win | 72.4316 |
| net_avg_loss | -82.4337 |
| avg_hold_time_bars | 12.6476 |
| exposure | 0.3954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
