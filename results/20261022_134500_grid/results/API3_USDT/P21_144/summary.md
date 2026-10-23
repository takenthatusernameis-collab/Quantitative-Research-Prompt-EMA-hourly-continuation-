# EMA Hourly Continuation — API3/USDT P21_144

**Symbol:** API3/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.6381 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8681 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -3.4331 |
| sortino_ratio | -1.1133 |
| max_drawdown | 0.7526 |
| cagr | -0.4066 |
| net_avg_win | 53.4245 |
| net_avg_loss | -70.5551 |
| avg_hold_time_bars | 22.4061 |
| exposure | 0.5367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
