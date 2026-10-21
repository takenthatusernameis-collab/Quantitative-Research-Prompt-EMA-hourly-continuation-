# EMA Hourly Continuation — GRT/USDT P8_89

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.8720 |
| net_win_rate | 0.5182 |
| gross_profit_factor | 1.0658 |
| gross_win_rate | 0.5182 |
| sharpe_ratio | -0.9855 |
| sortino_ratio | -0.3225 |
| max_drawdown | 0.4066 |
| cagr | -0.1413 |
| net_avg_win | 80.4925 |
| net_avg_loss | -99.2968 |
| avg_hold_time_bars | 25.5182 |
| exposure | 0.6016 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
