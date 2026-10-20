# EMA Hourly Continuation — ETN/USDT P50_144

**Symbol:** ETN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.4805 |
| net_win_rate | 0.4118 |
| gross_profit_factor | 0.7363 |
| gross_win_rate | 0.4250 |
| sharpe_ratio | -6.2428 |
| sortino_ratio | -2.1832 |
| max_drawdown | 0.9034 |
| cagr | -0.6638 |
| net_avg_win | 38.3079 |
| net_avg_loss | -55.8087 |
| avg_hold_time_bars | 8.9715 |
| exposure | 0.2568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
