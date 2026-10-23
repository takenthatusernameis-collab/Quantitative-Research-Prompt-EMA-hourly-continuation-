# EMA Hourly Continuation — MOG/USDT P26_89

**Symbol:** MOG/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.6994 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9550 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -3.2519 |
| sortino_ratio | -1.2144 |
| max_drawdown | 0.7617 |
| cagr | -0.4384 |
| net_avg_win | 54.3871 |
| net_avg_loss | -74.4480 |
| avg_hold_time_bars | 9.4346 |
| exposure | 0.3011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
