# EMA Hourly Continuation — ETN/USDT P8_26

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1365 |
| net_profit_factor | 0.2968 |
| net_win_rate | 0.3458 |
| gross_profit_factor | 0.4614 |
| gross_win_rate | 0.3575 |
| sharpe_ratio | -15.1118 |
| sortino_ratio | -8.5727 |
| max_drawdown | 0.9999 |
| cagr | -0.9885 |
| net_avg_win | 8.9395 |
| net_avg_loss | -15.9223 |
| avg_hold_time_bars | 3.8696 |
| exposure | 0.2869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
