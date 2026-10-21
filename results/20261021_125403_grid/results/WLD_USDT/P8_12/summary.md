# EMA Hourly Continuation — WLD/USDT P8_12

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 186 |
| net_profit_factor | 0.9597 |
| net_win_rate | 0.5591 |
| gross_profit_factor | 1.2552 |
| gross_win_rate | 0.5591 |
| sharpe_ratio | -0.1322 |
| sortino_ratio | -0.0263 |
| max_drawdown | 0.1406 |
| cagr | -0.0149 |
| net_avg_win | 84.8652 |
| net_avg_loss | -112.1483 |
| avg_hold_time_bars | 4.2258 |
| exposure | 0.0357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
