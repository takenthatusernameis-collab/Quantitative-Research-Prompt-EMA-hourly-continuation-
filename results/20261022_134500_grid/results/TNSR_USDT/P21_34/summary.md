# EMA Hourly Continuation — TNSR/USDT P21_34

**Symbol:** TNSR/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1111 |
| net_profit_factor | 0.5638 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 1.0057 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -8.2009 |
| sortino_ratio | -3.8357 |
| max_drawdown | 0.9921 |
| cagr | -0.8518 |
| net_avg_win | 25.5951 |
| net_avg_loss | -37.2823 |
| avg_hold_time_bars | 2.7282 |
| exposure | 0.1372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
