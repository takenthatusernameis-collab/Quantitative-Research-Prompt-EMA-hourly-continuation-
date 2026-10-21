# EMA Hourly Continuation — YFI/USDT P21_34

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.5415 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9334 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -3.9093 |
| sortino_ratio | -1.1687 |
| max_drawdown | 0.7412 |
| cagr | -0.4127 |
| net_avg_win | 42.1590 |
| net_avg_loss | -72.2672 |
| avg_hold_time_bars | 4.8209 |
| exposure | 0.0938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
