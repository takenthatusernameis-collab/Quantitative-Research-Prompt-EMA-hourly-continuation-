# EMA Hourly Continuation — SNX/USDT P21_144

**Symbol:** SNX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.9181 |
| net_win_rate | 0.5275 |
| gross_profit_factor | 1.1136 |
| gross_win_rate | 0.5275 |
| sharpe_ratio | -0.5182 |
| sortino_ratio | -0.1491 |
| max_drawdown | 0.2814 |
| cagr | -0.0708 |
| net_avg_win | 89.8803 |
| net_avg_loss | -109.2905 |
| avg_hold_time_bars | 26.8125 |
| exposure | 0.4853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
