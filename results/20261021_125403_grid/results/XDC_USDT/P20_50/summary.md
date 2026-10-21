# EMA Hourly Continuation — XDC/USDT P20_50

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.5461 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.8780 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -3.6046 |
| sortino_ratio | -1.0465 |
| max_drawdown | 0.7014 |
| cagr | -0.3807 |
| net_avg_win | 43.8497 |
| net_avg_loss | -70.3973 |
| avg_hold_time_bars | 9.2190 |
| exposure | 0.1722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
