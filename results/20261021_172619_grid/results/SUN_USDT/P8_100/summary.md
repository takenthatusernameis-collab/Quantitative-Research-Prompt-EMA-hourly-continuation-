# EMA Hourly Continuation — SUN/USDT P8_100

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.5900 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.9192 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -4.6395 |
| sortino_ratio | -1.4571 |
| max_drawdown | 0.8466 |
| cagr | -0.5040 |
| net_avg_win | 53.5156 |
| net_avg_loss | -74.0959 |
| avg_hold_time_bars | 29.2278 |
| exposure | 0.6560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
