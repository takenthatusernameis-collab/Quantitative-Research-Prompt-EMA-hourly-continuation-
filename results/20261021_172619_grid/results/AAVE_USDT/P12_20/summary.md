# EMA Hourly Continuation — AAVE/USDT P12_20

**Symbol:** AAVE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.5763 |
| net_win_rate | 0.4328 |
| gross_profit_factor | 0.7891 |
| gross_win_rate | 0.4328 |
| sharpe_ratio | -2.8171 |
| sortino_ratio | -0.6189 |
| max_drawdown | 0.5109 |
| cagr | -0.2478 |
| net_avg_win | 67.4640 |
| net_avg_loss | -89.3164 |
| avg_hold_time_bars | 6.0588 |
| exposure | 0.0655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
