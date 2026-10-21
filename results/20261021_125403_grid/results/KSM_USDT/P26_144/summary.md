# EMA Hourly Continuation — KSM/USDT P26_144

**Symbol:** KSM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.7983 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0063 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -1.3581 |
| sortino_ratio | -0.3543 |
| max_drawdown | 0.4019 |
| cagr | -0.1517 |
| net_avg_win | 80.2036 |
| net_avg_loss | -101.0773 |
| avg_hold_time_bars | 34.6156 |
| exposure | 0.5240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
