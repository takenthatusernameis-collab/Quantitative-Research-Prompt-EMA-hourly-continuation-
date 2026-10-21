# EMA Hourly Continuation — DEGEN/USDT P20_100

**Symbol:** DEGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.9408 |
| net_win_rate | 0.5251 |
| gross_profit_factor | 1.1045 |
| gross_win_rate | 0.5251 |
| sharpe_ratio | -0.4277 |
| sortino_ratio | -0.1348 |
| max_drawdown | 0.3063 |
| cagr | -0.0664 |
| net_avg_win | 100.1693 |
| net_avg_loss | -117.7307 |
| avg_hold_time_bars | 18.5921 |
| exposure | 0.4046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
