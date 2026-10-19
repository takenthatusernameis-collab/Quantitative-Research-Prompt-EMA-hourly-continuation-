# EMA Hourly Continuation — ETHFI/USDT P20_100

**Symbol:** ETHFI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.7060 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 1.0045 |
| gross_win_rate | 0.4955 |
| sharpe_ratio | -3.0092 |
| sortino_ratio | -1.0987 |
| max_drawdown | 0.7272 |
| cagr | -0.4039 |
| net_avg_win | 53.8983 |
| net_avg_loss | -72.7501 |
| avg_hold_time_bars | 14.9367 |
| exposure | 0.4508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
