# EMA Hourly Continuation — ZK/USDT P26_100

**Symbol:** ZK/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.8274 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0112 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.3465 |
| sortino_ratio | -0.4302 |
| max_drawdown | 0.3857 |
| cagr | -0.1816 |
| net_avg_win | 77.0537 |
| net_avg_loss | -93.9311 |
| avg_hold_time_bars | 14.3125 |
| exposure | 0.3238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
