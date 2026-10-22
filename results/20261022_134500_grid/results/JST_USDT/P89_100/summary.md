# EMA Hourly Continuation — JST/USDT P89_100

**Symbol:** JST/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.0927 |
| net_win_rate | 0.2897 |
| gross_profit_factor | 0.7867 |
| gross_win_rate | 0.4262 |
| sharpe_ratio | -12.0321 |
| sortino_ratio | -4.3739 |
| max_drawdown | 0.9978 |
| cagr | -0.9110 |
| net_avg_win | 6.4928 |
| net_avg_loss | -28.5637 |
| avg_hold_time_bars | 3.0000 |
| exposure | 0.0736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
