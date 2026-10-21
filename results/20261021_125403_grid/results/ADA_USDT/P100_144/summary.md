# EMA Hourly Continuation — ADA/USDT P100_144

**Symbol:** ADA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 194 |
| net_profit_factor | 0.6347 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.8945 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -1.8377 |
| sortino_ratio | -0.3669 |
| max_drawdown | 0.3439 |
| cagr | -0.1545 |
| net_avg_win | 64.2463 |
| net_avg_loss | -93.2060 |
| avg_hold_time_bars | 6.8196 |
| exposure | 0.0601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
