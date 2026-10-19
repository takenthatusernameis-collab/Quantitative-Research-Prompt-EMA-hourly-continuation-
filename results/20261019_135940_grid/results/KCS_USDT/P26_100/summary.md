# EMA Hourly Continuation — KCS/USDT P26_100

**Symbol:** KCS/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.2386 |
| net_win_rate | 0.3606 |
| gross_profit_factor | 0.6616 |
| gross_win_rate | 0.4136 |
| sharpe_ratio | -9.7314 |
| sortino_ratio | -3.5806 |
| max_drawdown | 0.9909 |
| cagr | -0.8447 |
| net_avg_win | 13.0467 |
| net_avg_loss | -30.8344 |
| avg_hold_time_bars | 11.9848 |
| exposure | 0.3595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
