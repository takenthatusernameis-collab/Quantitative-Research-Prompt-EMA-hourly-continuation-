# EMA Hourly Continuation — 1INCH/USDT P21_50

**Symbol:** 1INCH/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1049 |
| net_profit_factor | 0.4336 |
| net_win_rate | 0.4194 |
| gross_profit_factor | 0.8067 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -8.8289 |
| sortino_ratio | -4.0625 |
| max_drawdown | 0.9931 |
| cagr | -0.8620 |
| net_avg_win | 17.2787 |
| net_avg_loss | -28.7907 |
| avg_hold_time_bars | 4.4938 |
| exposure | 0.2143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
