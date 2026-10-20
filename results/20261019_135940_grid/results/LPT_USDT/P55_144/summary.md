# EMA Hourly Continuation — LPT/USDT P55_144

**Symbol:** LPT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.5880 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.8826 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -3.5988 |
| sortino_ratio | -1.1440 |
| max_drawdown | 0.7417 |
| cagr | -0.4136 |
| net_avg_win | 44.4586 |
| net_avg_loss | -67.1146 |
| avg_hold_time_bars | 11.1310 |
| exposure | 0.2550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
