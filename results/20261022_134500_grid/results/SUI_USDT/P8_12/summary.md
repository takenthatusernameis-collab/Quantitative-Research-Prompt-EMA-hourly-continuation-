# EMA Hourly Continuation — SUI/USDT P8_12

**Symbol:** SUI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1846 |
| net_profit_factor | 0.2877 |
| net_win_rate | 0.3608 |
| gross_profit_factor | 0.8004 |
| gross_win_rate | 0.4020 |
| sharpe_ratio | -18.4018 |
| sortino_ratio | -11.4481 |
| max_drawdown | 1.0000 |
| cagr | -0.9981 |
| net_avg_win | 6.0650 |
| net_avg_loss | -11.8977 |
| avg_hold_time_bars | 1.6219 |
| exposure | 0.1361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
