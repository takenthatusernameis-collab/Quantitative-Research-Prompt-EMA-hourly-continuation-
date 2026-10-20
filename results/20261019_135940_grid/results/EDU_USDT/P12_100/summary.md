# EMA Hourly Continuation — EDU/USDT P12_100

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 777 |
| net_profit_factor | 0.6499 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.8793 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -3.6563 |
| sortino_ratio | -1.4358 |
| max_drawdown | 0.8234 |
| cagr | -0.4905 |
| net_avg_win | 41.6914 |
| net_avg_loss | -56.5389 |
| avg_hold_time_bars | 15.7851 |
| exposure | 0.5550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
