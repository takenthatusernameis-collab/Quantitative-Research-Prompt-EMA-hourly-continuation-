# EMA Hourly Continuation — BLUR/USDT P55_89

**Symbol:** BLUR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.8741 |
| net_win_rate | 0.5441 |
| gross_profit_factor | 1.1934 |
| gross_win_rate | 0.5441 |
| sharpe_ratio | -0.7861 |
| sortino_ratio | -0.2062 |
| max_drawdown | 0.3415 |
| cagr | -0.0922 |
| net_avg_win | 83.9963 |
| net_avg_loss | -114.6666 |
| avg_hold_time_bars | 6.6413 |
| exposure | 0.0989 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
