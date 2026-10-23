# EMA Hourly Continuation — AVA/USDT P21_144

**Symbol:** AVA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.5786 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 0.8692 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -3.2478 |
| sortino_ratio | -1.0733 |
| max_drawdown | 0.7366 |
| cagr | -0.4014 |
| net_avg_win | 37.3941 |
| net_avg_loss | -60.5288 |
| avg_hold_time_bars | 18.9218 |
| exposure | 0.4730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
