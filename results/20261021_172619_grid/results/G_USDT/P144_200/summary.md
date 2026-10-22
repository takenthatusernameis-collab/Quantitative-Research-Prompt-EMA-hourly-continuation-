# EMA Hourly Continuation — G/USDT P144_200

**Symbol:** G/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 215 |
| net_profit_factor | 0.6848 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0391 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -1.9046 |
| sortino_ratio | -0.4319 |
| max_drawdown | 0.3597 |
| cagr | -0.1792 |
| net_avg_win | 69.4963 |
| net_avg_loss | -104.3604 |
| avg_hold_time_bars | 6.4465 |
| exposure | 0.0729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
