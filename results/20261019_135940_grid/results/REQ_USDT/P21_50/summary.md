# EMA Hourly Continuation — REQ/USDT P21_50

**Symbol:** REQ/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.4176 |
| net_win_rate | 0.4028 |
| gross_profit_factor | 0.8934 |
| gross_win_rate | 0.4409 |
| sharpe_ratio | -10.8413 |
| sortino_ratio | -5.0899 |
| max_drawdown | 0.9984 |
| cagr | -0.9231 |
| net_avg_win | 16.5332 |
| net_avg_loss | -26.7024 |
| avg_hold_time_bars | 5.2670 |
| exposure | 0.2574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
