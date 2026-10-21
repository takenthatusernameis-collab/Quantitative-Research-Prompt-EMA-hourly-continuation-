# EMA Hourly Continuation — KSM/USDT P100_144

**Symbol:** KSM/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.6461 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 0.9309 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -2.2488 |
| sortino_ratio | -0.5198 |
| max_drawdown | 0.4894 |
| cagr | -0.2122 |
| net_avg_win | 65.8244 |
| net_avg_loss | -94.3267 |
| avg_hold_time_bars | 6.0269 |
| exposure | 0.0712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
