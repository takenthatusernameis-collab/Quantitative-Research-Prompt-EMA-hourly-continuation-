# EMA Hourly Continuation — ETH/USDT P8_89

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.4562 |
| net_win_rate | 0.4387 |
| gross_profit_factor | 0.8733 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -6.6410 |
| sortino_ratio | -2.4102 |
| max_drawdown | 0.9559 |
| cagr | -0.7083 |
| net_avg_win | 26.9668 |
| net_avg_loss | -46.1999 |
| avg_hold_time_bars | 20.4697 |
| exposure | 0.6299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
