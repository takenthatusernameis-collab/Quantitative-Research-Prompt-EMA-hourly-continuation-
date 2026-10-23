# EMA Hourly Continuation — ETN/USDT P100_200

**Symbol:** ETN/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.4431 |
| net_win_rate | 0.3894 |
| gross_profit_factor | 0.6668 |
| gross_win_rate | 0.4009 |
| sharpe_ratio | -6.2154 |
| sortino_ratio | -2.0062 |
| max_drawdown | 0.8696 |
| cagr | -0.6155 |
| net_avg_win | 40.7681 |
| net_avg_loss | -58.6727 |
| avg_hold_time_bars | 8.3410 |
| exposure | 0.1966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
