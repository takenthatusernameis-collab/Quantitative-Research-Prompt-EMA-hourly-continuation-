# EMA Hourly Continuation — METIS/USDT P21_50

**Symbol:** METIS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.7084 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9435 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -2.5827 |
| sortino_ratio | -0.8543 |
| max_drawdown | 0.6510 |
| cagr | -0.3238 |
| net_avg_win | 58.6774 |
| net_avg_loss | -77.7317 |
| avg_hold_time_bars | 7.0822 |
| exposure | 0.1722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
