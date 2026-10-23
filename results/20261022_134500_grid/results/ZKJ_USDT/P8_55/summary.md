# EMA Hourly Continuation — ZKJ/USDT P8_55

**Symbol:** ZKJ/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.1863 |
| net_win_rate | 0.2653 |
| gross_profit_factor | 0.5399 |
| gross_win_rate | 0.3673 |
| sharpe_ratio | -12.1015 |
| sortino_ratio | -4.3117 |
| max_drawdown | 0.9974 |
| cagr | -0.9047 |
| net_avg_win | 15.9632 |
| net_avg_loss | -30.9480 |
| avg_hold_time_bars | 31.8534 |
| exposure | 0.7804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
