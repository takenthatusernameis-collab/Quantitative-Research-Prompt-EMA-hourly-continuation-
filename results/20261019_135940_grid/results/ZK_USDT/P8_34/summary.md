# EMA Hourly Continuation — ZK/USDT P8_34

**Symbol:** ZK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1345 |
| net_profit_factor | 0.6263 |
| net_win_rate | 0.4572 |
| gross_profit_factor | 0.9549 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -7.2784 |
| sortino_ratio | -3.9098 |
| max_drawdown | 0.9872 |
| cagr | -0.8437 |
| net_avg_win | 26.9022 |
| net_avg_loss | -36.1852 |
| avg_hold_time_bars | 5.1286 |
| exposure | 0.3363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
