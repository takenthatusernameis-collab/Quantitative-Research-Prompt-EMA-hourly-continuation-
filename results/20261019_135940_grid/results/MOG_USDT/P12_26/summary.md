# EMA Hourly Continuation — MOG/USDT P12_26

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1289 |
| net_profit_factor | 0.6679 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.9912 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -7.4683 |
| sortino_ratio | -3.9448 |
| max_drawdown | 0.9878 |
| cagr | -0.8530 |
| net_avg_win | 33.0588 |
| net_avg_loss | -43.2352 |
| avg_hold_time_bars | 3.1862 |
| exposure | 0.2042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
