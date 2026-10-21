# EMA Hourly Continuation — SSV/USDT P12_100

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7102 |
| net_win_rate | 0.4544 |
| gross_profit_factor | 0.8538 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -2.5837 |
| sortino_ratio | -0.8112 |
| max_drawdown | 0.6511 |
| cagr | -0.3120 |
| net_avg_win | 66.8183 |
| net_avg_loss | -78.3443 |
| avg_hold_time_bars | 25.8600 |
| exposure | 0.5769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
