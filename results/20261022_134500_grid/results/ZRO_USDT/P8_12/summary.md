# EMA Hourly Continuation — ZRO/USDT P8_12

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1760 |
| net_profit_factor | 0.3015 |
| net_win_rate | 0.3722 |
| gross_profit_factor | 0.6971 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -16.9015 |
| sortino_ratio | -10.4802 |
| max_drawdown | 1.0000 |
| cagr | -0.9963 |
| net_avg_win | 6.5907 |
| net_avg_loss | -12.9564 |
| avg_hold_time_bars | 1.6716 |
| exposure | 0.1440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
