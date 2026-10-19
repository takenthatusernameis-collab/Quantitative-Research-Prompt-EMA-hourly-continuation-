# EMA Hourly Continuation — NEO/USDT P12_34

**Symbol:** NEO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1290 |
| net_profit_factor | 0.3551 |
| net_win_rate | 0.4031 |
| gross_profit_factor | 0.7594 |
| gross_win_rate | 0.4318 |
| sharpe_ratio | -11.3563 |
| sortino_ratio | -5.7755 |
| max_drawdown | 0.9993 |
| cagr | -0.9456 |
| net_avg_win | 10.5811 |
| net_avg_loss | -20.1240 |
| avg_hold_time_bars | 4.1496 |
| exposure | 0.2433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
