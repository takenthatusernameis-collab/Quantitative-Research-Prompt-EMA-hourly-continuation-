# EMA Hourly Continuation — ZKJ/USDT P20_89

**Symbol:** ZKJ/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.1731 |
| net_win_rate | 0.2935 |
| gross_profit_factor | 0.4516 |
| gross_win_rate | 0.3632 |
| sharpe_ratio | -9.7648 |
| sortino_ratio | -2.9396 |
| max_drawdown | 0.9832 |
| cagr | -0.8014 |
| net_avg_win | 17.4338 |
| net_avg_loss | -41.8473 |
| avg_hold_time_bars | 42.1567 |
| exposure | 0.7703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
