# EMA Hourly Continuation — ERG/USDT P89_144

**Symbol:** ERG/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.3213 |
| net_win_rate | 0.3733 |
| gross_profit_factor | 0.6339 |
| gross_win_rate | 0.3924 |
| sharpe_ratio | -7.5766 |
| sortino_ratio | -2.4763 |
| max_drawdown | 0.9553 |
| cagr | -0.7100 |
| net_avg_win | 23.0799 |
| net_avg_loss | -42.7874 |
| avg_hold_time_bars | 4.8000 |
| exposure | 0.1145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
