# EMA Hourly Continuation — FET/USDT P20_100

**Symbol:** FET/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.8664 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0244 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -0.8431 |
| sortino_ratio | -0.2424 |
| max_drawdown | 0.2784 |
| cagr | -0.1084 |
| net_avg_win | 79.5448 |
| net_avg_loss | -94.5953 |
| avg_hold_time_bars | 24.3259 |
| exposure | 0.4445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
