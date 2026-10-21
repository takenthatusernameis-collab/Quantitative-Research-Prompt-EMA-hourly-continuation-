# EMA Hourly Continuation — SUN/USDT P21_144

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.4987 |
| net_win_rate | 0.4079 |
| gross_profit_factor | 0.7691 |
| gross_win_rate | 0.4306 |
| sharpe_ratio | -4.4390 |
| sortino_ratio | -1.1760 |
| max_drawdown | 0.7606 |
| cagr | -0.4304 |
| net_avg_win | 52.3774 |
| net_avg_loss | -72.3658 |
| avg_hold_time_bars | 35.5297 |
| exposure | 0.5676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
