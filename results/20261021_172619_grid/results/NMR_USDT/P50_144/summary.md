# EMA Hourly Continuation — NMR/USDT P50_144

**Symbol:** NMR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.7789 |
| net_win_rate | 0.5089 |
| gross_profit_factor | 1.0110 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -1.4514 |
| sortino_ratio | -0.4139 |
| max_drawdown | 0.4196 |
| cagr | -0.1736 |
| net_avg_win | 66.7053 |
| net_avg_loss | -88.7294 |
| avg_hold_time_bars | 14.5063 |
| exposure | 0.2605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
