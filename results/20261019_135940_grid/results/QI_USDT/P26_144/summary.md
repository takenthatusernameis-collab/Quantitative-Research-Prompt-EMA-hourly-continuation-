# EMA Hourly Continuation — QI/USDT P26_144

**Symbol:** QI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.5574 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8808 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -4.0197 |
| sortino_ratio | -1.2695 |
| max_drawdown | 0.8017 |
| cagr | -0.4594 |
| net_avg_win | 42.7812 |
| net_avg_loss | -63.8218 |
| avg_hold_time_bars | 18.8043 |
| exposure | 0.4348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
