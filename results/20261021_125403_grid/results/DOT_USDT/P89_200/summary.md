# EMA Hourly Continuation — DOT/USDT P89_200

**Symbol:** DOT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.7685 |
| net_win_rate | 0.5058 |
| gross_profit_factor | 1.0124 |
| gross_win_rate | 0.5058 |
| sharpe_ratio | -1.2565 |
| sortino_ratio | -0.2892 |
| max_drawdown | 0.2898 |
| cagr | -0.1248 |
| net_avg_win | 72.6391 |
| net_avg_loss | -96.7498 |
| avg_hold_time_bars | 13.7315 |
| exposure | 0.1604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
