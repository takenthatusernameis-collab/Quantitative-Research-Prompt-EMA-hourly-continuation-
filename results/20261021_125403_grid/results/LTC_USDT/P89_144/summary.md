# EMA Hourly Continuation — LTC/USDT P89_144

**Symbol:** LTC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.6671 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0034 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.8060 |
| sortino_ratio | -0.3989 |
| max_drawdown | 0.3793 |
| cagr | -0.1658 |
| net_avg_win | 61.5965 |
| net_avg_loss | -94.7238 |
| avg_hold_time_bars | 7.8553 |
| exposure | 0.0839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
