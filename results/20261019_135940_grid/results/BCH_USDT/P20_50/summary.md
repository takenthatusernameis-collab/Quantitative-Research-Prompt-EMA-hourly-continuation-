# EMA Hourly Continuation — BCH/USDT P20_50

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 964 |
| net_profit_factor | 0.3934 |
| net_win_rate | 0.4346 |
| gross_profit_factor | 0.8552 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -9.1997 |
| sortino_ratio | -4.0374 |
| max_drawdown | 0.9942 |
| cagr | -0.8708 |
| net_avg_win | 15.3892 |
| net_avg_loss | -30.0724 |
| avg_hold_time_bars | 5.2884 |
| exposure | 0.2317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
