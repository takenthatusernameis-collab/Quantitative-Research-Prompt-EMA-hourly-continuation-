# EMA Hourly Continuation — HTX/USDT P34_144

**Symbol:** HTX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.3986 |
| net_win_rate | 0.3523 |
| gross_profit_factor | 0.8651 |
| gross_win_rate | 0.4012 |
| sharpe_ratio | -8.6779 |
| sortino_ratio | -2.8194 |
| max_drawdown | 0.9780 |
| cagr | -0.7744 |
| net_avg_win | 35.9612 |
| net_avg_loss | -49.0612 |
| avg_hold_time_bars | 19.5382 |
| exposure | 0.4518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
