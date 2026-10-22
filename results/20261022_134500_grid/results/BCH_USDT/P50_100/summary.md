# EMA Hourly Continuation — BCH/USDT P50_100

**Symbol:** BCH/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.4469 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8622 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -6.4173 |
| sortino_ratio | -2.3087 |
| max_drawdown | 0.9412 |
| cagr | -0.6730 |
| net_avg_win | 26.7343 |
| net_avg_loss | -47.8556 |
| avg_hold_time_bars | 6.0047 |
| exposure | 0.1744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
