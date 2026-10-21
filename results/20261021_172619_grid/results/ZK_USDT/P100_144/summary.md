# EMA Hourly Continuation — ZK/USDT P100_144

**Symbol:** ZK/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.7767 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0193 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -1.3370 |
| sortino_ratio | -0.3156 |
| max_drawdown | 0.3372 |
| cagr | -0.1353 |
| net_avg_win | 79.0448 |
| net_avg_loss | -103.3926 |
| avg_hold_time_bars | 8.2738 |
| exposure | 0.1017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
