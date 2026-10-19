# EMA Hourly Continuation — XMR/USDT P8_200

**Symbol:** XMR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.5084 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.9312 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -5.3969 |
| sortino_ratio | -1.9424 |
| max_drawdown | 0.9147 |
| cagr | -0.6223 |
| net_avg_win | 30.6667 |
| net_avg_loss | -51.1804 |
| avg_hold_time_bars | 23.4516 |
| exposure | 0.7153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
