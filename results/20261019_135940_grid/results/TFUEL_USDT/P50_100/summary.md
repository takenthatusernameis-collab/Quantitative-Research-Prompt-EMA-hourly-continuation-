# EMA Hourly Continuation — TFUEL/USDT P50_100

**Symbol:** TFUEL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.4306 |
| net_win_rate | 0.3917 |
| gross_profit_factor | 0.7856 |
| gross_win_rate | 0.4078 |
| sharpe_ratio | -8.1947 |
| sortino_ratio | -3.1625 |
| max_drawdown | 0.9801 |
| cagr | -0.7877 |
| net_avg_win | 25.4706 |
| net_avg_loss | -38.0783 |
| avg_hold_time_bars | 5.5141 |
| exposure | 0.1854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
