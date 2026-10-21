# EMA Hourly Continuation — YFI/USDT P12_50

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.5683 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.8637 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -4.8806 |
| sortino_ratio | -1.9137 |
| max_drawdown | 0.8939 |
| cagr | -0.5840 |
| net_avg_win | 33.7850 |
| net_avg_loss | -50.6855 |
| avg_hold_time_bars | 9.0650 |
| exposure | 0.3093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
