# EMA Hourly Continuation — W/USDT P21_89

**Symbol:** W/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.8543 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0332 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -1.1058 |
| sortino_ratio | -0.3528 |
| max_drawdown | 0.3998 |
| cagr | -0.1526 |
| net_avg_win | 79.1761 |
| net_avg_loss | -96.1066 |
| avg_hold_time_bars | 16.2667 |
| exposure | 0.3660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
