# EMA Hourly Continuation — ACE/USDT P55_89

**Symbol:** ACE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7608 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0503 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -1.6300 |
| sortino_ratio | -0.4329 |
| max_drawdown | 0.4311 |
| cagr | -0.1801 |
| net_avg_win | 71.5805 |
| net_avg_loss | -98.0108 |
| avg_hold_time_bars | 7.8134 |
| exposure | 0.1213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
