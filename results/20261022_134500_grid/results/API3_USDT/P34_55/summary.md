# EMA Hourly Continuation — API3/USDT P34_55

**Symbol:** API3/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 922 |
| net_profit_factor | 0.5235 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.9923 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -7.4108 |
| sortino_ratio | -3.2012 |
| max_drawdown | 0.9801 |
| cagr | -0.7875 |
| net_avg_win | 25.9309 |
| net_avg_loss | -40.5457 |
| avg_hold_time_bars | 3.5564 |
| exposure | 0.1490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
