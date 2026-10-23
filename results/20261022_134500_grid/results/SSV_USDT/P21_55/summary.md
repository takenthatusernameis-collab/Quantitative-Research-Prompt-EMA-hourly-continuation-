# EMA Hourly Continuation — SSV/USDT P21_55

**Symbol:** SSV/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1034 |
| net_profit_factor | 0.5486 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.8662 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -7.0197 |
| sortino_ratio | -3.1639 |
| max_drawdown | 0.9807 |
| cagr | -0.7847 |
| net_avg_win | 25.9847 |
| net_avg_loss | -37.6618 |
| avg_hold_time_bars | 5.2843 |
| exposure | 0.2473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
