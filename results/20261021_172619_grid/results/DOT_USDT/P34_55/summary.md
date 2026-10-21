# EMA Hourly Continuation — DOT/USDT P34_55

**Symbol:** DOT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.9287 |
| net_win_rate | 0.5725 |
| gross_profit_factor | 1.3271 |
| gross_win_rate | 0.5725 |
| sharpe_ratio | -0.3303 |
| sortino_ratio | -0.0781 |
| max_drawdown | 0.1786 |
| cagr | -0.0381 |
| net_avg_win | 80.7881 |
| net_avg_loss | -116.5032 |
| avg_hold_time_bars | 5.7748 |
| exposure | 0.0688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
