# EMA Hourly Continuation — ZK/USDT P12_55

**Symbol:** ZK/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.8548 |
| net_win_rate | 0.5098 |
| gross_profit_factor | 1.0594 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -1.4457 |
| sortino_ratio | -0.5316 |
| max_drawdown | 0.5425 |
| cagr | -0.2191 |
| net_avg_win | 82.9625 |
| net_avg_loss | -100.9314 |
| avg_hold_time_bars | 12.1062 |
| exposure | 0.3612 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
