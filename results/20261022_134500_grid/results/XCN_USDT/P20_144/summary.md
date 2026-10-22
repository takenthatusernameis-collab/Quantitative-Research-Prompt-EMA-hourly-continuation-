# EMA Hourly Continuation — XCN/USDT P20_144

**Symbol:** XCN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.5376 |
| net_win_rate | 0.4296 |
| gross_profit_factor | 0.8278 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -5.6457 |
| sortino_ratio | -2.0441 |
| max_drawdown | 0.9170 |
| cagr | -0.6284 |
| net_avg_win | 37.1435 |
| net_avg_loss | -52.0415 |
| avg_hold_time_bars | 17.3249 |
| exposure | 0.5260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
