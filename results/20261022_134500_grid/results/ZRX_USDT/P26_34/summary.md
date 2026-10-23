# EMA Hourly Continuation — ZRX/USDT P26_34

**Symbol:** ZRX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1084 |
| net_profit_factor | 0.2528 |
| net_win_rate | 0.3782 |
| gross_profit_factor | 0.7105 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -12.5553 |
| sortino_ratio | -5.9569 |
| max_drawdown | 0.9996 |
| cagr | -0.9548 |
| net_avg_win | 8.2501 |
| net_avg_loss | -19.8492 |
| avg_hold_time_bars | 2.6780 |
| exposure | 0.1320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
