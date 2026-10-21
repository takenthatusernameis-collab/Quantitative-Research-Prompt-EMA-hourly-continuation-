# EMA Hourly Continuation — XCH/USDT P144_200

**Symbol:** XCH/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 160 |
| net_profit_factor | 0.7270 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 0.9541 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -1.2644 |
| sortino_ratio | -0.2289 |
| max_drawdown | 0.2493 |
| cagr | -0.0999 |
| net_avg_win | 79.2714 |
| net_avg_loss | -103.7249 |
| avg_hold_time_bars | 8.1875 |
| exposure | 0.0595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
