# EMA Hourly Continuation — NUM/USDT P21_144

**Symbol:** NUM/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.5550 |
| net_win_rate | 0.4048 |
| gross_profit_factor | 0.7536 |
| gross_win_rate | 0.4067 |
| sharpe_ratio | -4.6375 |
| sortino_ratio | -1.4611 |
| max_drawdown | 0.8370 |
| cagr | -0.5013 |
| net_avg_win | 50.4853 |
| net_avg_loss | -61.8548 |
| avg_hold_time_bars | 23.5040 |
| exposure | 0.5385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
