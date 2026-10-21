# EMA Hourly Continuation — DOGS/USDT P50_144

**Symbol:** DOGS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.8639 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0514 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -0.8892 |
| sortino_ratio | -0.2308 |
| max_drawdown | 0.3056 |
| cagr | -0.1027 |
| net_avg_win | 92.3454 |
| net_avg_loss | -111.5722 |
| avg_hold_time_bars | 20.0536 |
| exposure | 0.2979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
