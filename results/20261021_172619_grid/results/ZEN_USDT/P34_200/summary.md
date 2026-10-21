# EMA Hourly Continuation — ZEN/USDT P34_200

**Symbol:** ZEN/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7731 |
| net_win_rate | 0.4867 |
| gross_profit_factor | 0.9361 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -1.4026 |
| sortino_ratio | -0.3683 |
| max_drawdown | 0.4063 |
| cagr | -0.1576 |
| net_avg_win | 72.2439 |
| net_avg_loss | -88.6165 |
| avg_hold_time_bars | 33.3215 |
| exposure | 0.5135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
