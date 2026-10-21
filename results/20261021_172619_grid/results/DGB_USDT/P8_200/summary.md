# EMA Hourly Continuation — DGB/USDT P8_200

**Symbol:** DGB/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7265 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.8602 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -1.9807 |
| sortino_ratio | -0.5414 |
| max_drawdown | 0.4972 |
| cagr | -0.2216 |
| net_avg_win | 72.0950 |
| net_avg_loss | -85.3472 |
| avg_hold_time_bars | 45.2930 |
| exposure | 0.7659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
