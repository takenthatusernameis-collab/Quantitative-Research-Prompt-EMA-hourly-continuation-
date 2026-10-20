# EMA Hourly Continuation — XEC/USDT P12_20

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1554 |
| net_profit_factor | 0.2505 |
| net_win_rate | 0.3803 |
| gross_profit_factor | 0.8523 |
| gross_win_rate | 0.4356 |
| sharpe_ratio | -15.3071 |
| sortino_ratio | -8.6533 |
| max_drawdown | 1.0000 |
| cagr | -0.9892 |
| net_avg_win | 5.6537 |
| net_avg_loss | -13.8538 |
| avg_hold_time_bars | 2.6718 |
| exposure | 0.1879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
