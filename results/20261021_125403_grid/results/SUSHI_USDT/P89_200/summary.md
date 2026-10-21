# EMA Hourly Continuation — SUSHI/USDT P89_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.7309 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9373 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -1.5888 |
| sortino_ratio | -0.3838 |
| max_drawdown | 0.3717 |
| cagr | -0.1618 |
| net_avg_win | 69.7253 |
| net_avg_loss | -90.8547 |
| avg_hold_time_bars | 13.6411 |
| exposure | 0.1772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
