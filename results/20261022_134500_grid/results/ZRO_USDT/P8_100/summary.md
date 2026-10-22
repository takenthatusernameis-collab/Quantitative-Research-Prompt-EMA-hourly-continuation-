# EMA Hourly Continuation — ZRO/USDT P8_100

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.7360 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0077 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -2.4264 |
| sortino_ratio | -0.8710 |
| max_drawdown | 0.6510 |
| cagr | -0.3438 |
| net_avg_win | 57.0074 |
| net_avg_loss | -78.4771 |
| avg_hold_time_bars | 22.0280 |
| exposure | 0.6555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
