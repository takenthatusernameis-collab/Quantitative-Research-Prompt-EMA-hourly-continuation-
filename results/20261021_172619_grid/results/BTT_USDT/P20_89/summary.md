# EMA Hourly Continuation — BTT/USDT P20_89

**Symbol:** BTT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.5094 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.7966 |
| gross_win_rate | 0.4234 |
| sharpe_ratio | -5.2902 |
| sortino_ratio | -1.5946 |
| max_drawdown | 0.8518 |
| cagr | -0.5309 |
| net_avg_win | 47.2268 |
| net_avg_loss | -67.4583 |
| avg_hold_time_bars | 21.0068 |
| exposure | 0.4240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
