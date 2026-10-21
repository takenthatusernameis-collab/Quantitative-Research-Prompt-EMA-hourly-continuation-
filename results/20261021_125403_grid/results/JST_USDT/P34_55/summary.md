# EMA Hourly Continuation — JST/USDT P34_55

**Symbol:** JST/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.4580 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 1.0656 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -4.2051 |
| sortino_ratio | -1.1360 |
| max_drawdown | 0.7479 |
| cagr | -0.4156 |
| net_avg_win | 35.6297 |
| net_avg_loss | -76.9213 |
| avg_hold_time_bars | 6.3136 |
| exposure | 0.1011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
