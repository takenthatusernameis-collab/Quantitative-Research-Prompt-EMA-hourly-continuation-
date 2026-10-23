# EMA Hourly Continuation — BAND/USDT P8_34

**Symbol:** BAND/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1209 |
| net_profit_factor | 0.5532 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.9940 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -7.0482 |
| sortino_ratio | -3.4367 |
| max_drawdown | 0.9854 |
| cagr | -0.8123 |
| net_avg_win | 21.5929 |
| net_avg_loss | -34.2438 |
| avg_hold_time_bars | 6.6336 |
| exposure | 0.3629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
