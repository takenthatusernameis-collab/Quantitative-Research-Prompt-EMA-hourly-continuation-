# EMA Hourly Continuation — RAY/USDT P8_20

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1633 |
| net_profit_factor | 0.5200 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.9722 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -9.9161 |
| sortino_ratio | -5.6259 |
| max_drawdown | 0.9991 |
| cagr | -0.9398 |
| net_avg_win | 14.7457 |
| net_avg_loss | -23.1532 |
| avg_hold_time_bars | 3.1157 |
| exposure | 0.2313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
