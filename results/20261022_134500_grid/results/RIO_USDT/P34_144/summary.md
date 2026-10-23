# EMA Hourly Continuation — RIO/USDT P34_144

**Symbol:** RIO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.5260 |
| net_win_rate | 0.4013 |
| gross_profit_factor | 0.7000 |
| gross_win_rate | 0.4030 |
| sharpe_ratio | -5.4457 |
| sortino_ratio | -1.8877 |
| max_drawdown | 0.9100 |
| cagr | -0.5987 |
| net_avg_win | 40.7813 |
| net_avg_loss | -51.9714 |
| avg_hold_time_bars | 13.3865 |
| exposure | 0.3737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
