# EMA Hourly Continuation — T/USDT P21_26

**Symbol:** T/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 930 |
| net_profit_factor | 0.3009 |
| net_win_rate | 0.3978 |
| gross_profit_factor | 0.8994 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -11.2769 |
| sortino_ratio | -4.9267 |
| max_drawdown | 0.9987 |
| cagr | -0.9275 |
| net_avg_win | 11.6189 |
| net_avg_loss | -25.5101 |
| avg_hold_time_bars | 3.2882 |
| exposure | 0.1384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
