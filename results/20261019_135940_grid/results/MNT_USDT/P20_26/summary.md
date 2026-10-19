# EMA Hourly Continuation — MNT/USDT P20_26

**Symbol:** MNT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1199 |
| net_profit_factor | 0.1580 |
| net_win_rate | 0.3244 |
| gross_profit_factor | 0.7107 |
| gross_win_rate | 0.4003 |
| sharpe_ratio | -16.5698 |
| sortino_ratio | -8.5734 |
| max_drawdown | 1.0000 |
| cagr | -0.9908 |
| net_avg_win | 4.8238 |
| net_avg_loss | -14.6622 |
| avg_hold_time_bars | 2.2252 |
| exposure | 0.1213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
