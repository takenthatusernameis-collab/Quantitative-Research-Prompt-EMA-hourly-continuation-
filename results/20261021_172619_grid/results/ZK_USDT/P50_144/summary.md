# EMA Hourly Continuation — ZK/USDT P50_144

**Symbol:** ZK/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7712 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9312 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -1.6145 |
| sortino_ratio | -0.4538 |
| max_drawdown | 0.4112 |
| cagr | -0.1893 |
| net_avg_win | 74.7658 |
| net_avg_loss | -90.7249 |
| avg_hold_time_bars | 16.0055 |
| exposure | 0.2825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
