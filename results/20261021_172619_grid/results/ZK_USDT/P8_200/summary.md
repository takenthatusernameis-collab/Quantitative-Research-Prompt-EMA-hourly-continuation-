# EMA Hourly Continuation — ZK/USDT P8_200

**Symbol:** ZK/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.8793 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0059 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -0.6697 |
| sortino_ratio | -0.1715 |
| max_drawdown | 0.2348 |
| cagr | -0.0786 |
| net_avg_win | 84.7202 |
| net_avg_loss | -97.6555 |
| avg_hold_time_bars | 54.4262 |
| exposure | 0.7907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
