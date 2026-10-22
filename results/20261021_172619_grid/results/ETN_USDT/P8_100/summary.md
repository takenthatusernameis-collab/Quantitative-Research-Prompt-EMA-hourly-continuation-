# EMA Hourly Continuation — ETN/USDT P8_100

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.5650 |
| net_win_rate | 0.4099 |
| gross_profit_factor | 0.6821 |
| gross_win_rate | 0.4099 |
| sharpe_ratio | -4.3382 |
| sortino_ratio | -1.4997 |
| max_drawdown | 0.7693 |
| cagr | -0.5005 |
| net_avg_win | 48.1520 |
| net_avg_loss | -59.2023 |
| avg_hold_time_bars | 18.9723 |
| exposure | 0.5204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
