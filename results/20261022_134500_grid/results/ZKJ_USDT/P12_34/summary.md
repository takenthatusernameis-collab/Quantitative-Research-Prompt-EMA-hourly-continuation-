# EMA Hourly Continuation — ZKJ/USDT P12_34

**Symbol:** ZKJ/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.1815 |
| net_win_rate | 0.1975 |
| gross_profit_factor | 0.4746 |
| gross_win_rate | 0.3343 |
| sharpe_ratio | -15.8961 |
| sortino_ratio | -6.8570 |
| max_drawdown | 0.9999 |
| cagr | -0.9776 |
| net_avg_win | 15.8345 |
| net_avg_loss | -21.4694 |
| avg_hold_time_bars | 21.3145 |
| exposure | 0.6869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
