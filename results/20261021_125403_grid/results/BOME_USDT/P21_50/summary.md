# EMA Hourly Continuation — BOME/USDT P21_50

**Symbol:** BOME/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7797 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 0.9777 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -1.6251 |
| sortino_ratio | -0.5094 |
| max_drawdown | 0.4972 |
| cagr | -0.2093 |
| net_avg_win | 65.9977 |
| net_avg_loss | -84.2885 |
| avg_hold_time_bars | 7.3340 |
| exposure | 0.1597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
