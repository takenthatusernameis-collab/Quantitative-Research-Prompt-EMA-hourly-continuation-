# EMA Hourly Continuation — ZRX/USDT P20_50

**Symbol:** ZRX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 973 |
| net_profit_factor | 0.4367 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7890 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -7.9542 |
| sortino_ratio | -3.5017 |
| max_drawdown | 0.9867 |
| cagr | -0.8197 |
| net_avg_win | 18.3414 |
| net_avg_loss | -31.4982 |
| avg_hold_time_bars | 5.5653 |
| exposure | 0.2461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
