# EMA Hourly Continuation — ZRX/USDT P12_26

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5939 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.8877 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -4.2798 |
| sortino_ratio | -1.5469 |
| max_drawdown | 0.8346 |
| cagr | -0.5076 |
| net_avg_win | 40.6603 |
| net_avg_loss | -60.7406 |
| avg_hold_time_bars | 5.5708 |
| exposure | 0.1610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
