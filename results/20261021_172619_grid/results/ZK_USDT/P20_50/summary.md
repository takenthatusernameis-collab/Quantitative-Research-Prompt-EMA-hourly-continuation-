# EMA Hourly Continuation — ZK/USDT P20_50

**Symbol:** ZK/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.8154 |
| net_win_rate | 0.5069 |
| gross_profit_factor | 1.0430 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -1.6190 |
| sortino_ratio | -0.5419 |
| max_drawdown | 0.5218 |
| cagr | -0.2209 |
| net_avg_win | 76.0920 |
| net_avg_loss | -95.9286 |
| avg_hold_time_bars | 7.5858 |
| exposure | 0.1875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
