# EMA Hourly Continuation — DYDX/USDT P8_12

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1813 |
| net_profit_factor | 0.1544 |
| net_win_rate | 0.3822 |
| gross_profit_factor | 0.5900 |
| gross_win_rate | 0.4231 |
| sharpe_ratio | -16.7317 |
| sortino_ratio | -10.2547 |
| max_drawdown | 1.0000 |
| cagr | -0.9955 |
| net_avg_win | 2.6345 |
| net_avg_loss | -10.5586 |
| avg_hold_time_bars | 1.9068 |
| exposure | 0.1571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
