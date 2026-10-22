# EMA Hourly Continuation — XCN/USDT P89_100

**Symbol:** XCN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 802 |
| net_profit_factor | 0.1679 |
| net_win_rate | 0.3042 |
| gross_profit_factor | 0.5792 |
| gross_win_rate | 0.3529 |
| sharpe_ratio | -13.4307 |
| sortino_ratio | -5.6338 |
| max_drawdown | 0.9995 |
| cagr | -0.9526 |
| net_avg_win | 8.2648 |
| net_avg_loss | -21.5267 |
| avg_hold_time_bars | 2.2095 |
| exposure | 0.0805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
