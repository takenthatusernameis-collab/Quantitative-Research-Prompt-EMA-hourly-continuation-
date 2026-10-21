# EMA Hourly Continuation — XDC/USDT P21_50

**Symbol:** XDC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.5577 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.9037 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -3.5043 |
| sortino_ratio | -1.0033 |
| max_drawdown | 0.6874 |
| cagr | -0.3680 |
| net_avg_win | 45.8869 |
| net_avg_loss | -73.3092 |
| avg_hold_time_bars | 8.6591 |
| exposure | 0.1570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
