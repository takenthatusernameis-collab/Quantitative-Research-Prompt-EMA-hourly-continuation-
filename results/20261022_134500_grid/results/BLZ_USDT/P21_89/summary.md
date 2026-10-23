# EMA Hourly Continuation — BLZ/USDT P21_89

**Symbol:** BLZ/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 780 |
| net_profit_factor | 0.5777 |
| net_win_rate | 0.4333 |
| gross_profit_factor | 0.8784 |
| gross_win_rate | 0.4397 |
| sharpe_ratio | -5.9222 |
| sortino_ratio | -2.3174 |
| max_drawdown | 0.9435 |
| cagr | -0.6732 |
| net_avg_win | 38.0565 |
| net_avg_loss | -50.3789 |
| avg_hold_time_bars | 11.2167 |
| exposure | 0.3959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
