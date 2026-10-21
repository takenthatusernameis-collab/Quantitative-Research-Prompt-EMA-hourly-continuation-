# EMA Hourly Continuation — LTC/USDT P100_200

**Symbol:** LTC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.5242 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.7556 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -2.8937 |
| sortino_ratio | -0.6618 |
| max_drawdown | 0.5401 |
| cagr | -0.2616 |
| net_avg_win | 51.5275 |
| net_avg_loss | -78.3581 |
| avg_hold_time_bars | 11.4125 |
| exposure | 0.1333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
