# EMA Hourly Continuation — CHZ/USDT P21_26

**Symbol:** CHZ/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 177 |
| net_profit_factor | 0.6655 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9570 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -1.6401 |
| sortino_ratio | -0.3135 |
| max_drawdown | 0.3370 |
| cagr | -0.1332 |
| net_avg_win | 68.9816 |
| net_avg_loss | -100.1927 |
| avg_hold_time_bars | 3.9322 |
| exposure | 0.0316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
