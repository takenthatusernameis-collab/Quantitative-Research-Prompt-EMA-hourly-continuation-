# EMA Hourly Continuation — ETN/USDT P8_20

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.4288 |
| net_win_rate | 0.3784 |
| gross_profit_factor | 0.5638 |
| gross_win_rate | 0.3784 |
| sharpe_ratio | -5.2819 |
| sortino_ratio | -1.6276 |
| max_drawdown | 0.7984 |
| cagr | -0.5315 |
| net_avg_win | 39.6189 |
| net_avg_loss | -56.2507 |
| avg_hold_time_bars | 6.3634 |
| exposure | 0.1379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
