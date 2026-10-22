# EMA Hourly Continuation — VR/USDT P8_144

**Symbol:** VR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.7822 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9111 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -1.4345 |
| sortino_ratio | -0.3854 |
| max_drawdown | 0.3638 |
| cagr | -0.1648 |
| net_avg_win | 76.4100 |
| net_avg_loss | -89.8057 |
| avg_hold_time_bars | 41.2913 |
| exposure | 0.6700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
