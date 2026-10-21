# EMA Hourly Continuation — JST/USDT P20_50

**Symbol:** JST/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.5021 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 1.0431 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -4.5405 |
| sortino_ratio | -1.4989 |
| max_drawdown | 0.8349 |
| cagr | -0.5040 |
| net_avg_win | 31.9338 |
| net_avg_loss | -61.9394 |
| avg_hold_time_bars | 7.6949 |
| exposure | 0.1849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
