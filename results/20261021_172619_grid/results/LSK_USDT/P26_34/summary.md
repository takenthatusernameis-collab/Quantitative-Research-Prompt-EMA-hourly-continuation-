# EMA Hourly Continuation — LSK/USDT P26_34

**Symbol:** LSK/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.5722 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 1.0068 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -3.5080 |
| sortino_ratio | -0.9775 |
| max_drawdown | 0.6842 |
| cagr | -0.3634 |
| net_avg_win | 50.1239 |
| net_avg_loss | -81.3072 |
| avg_hold_time_bars | 4.7527 |
| exposure | 0.0812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
