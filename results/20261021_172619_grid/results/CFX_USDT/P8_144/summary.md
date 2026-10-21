# EMA Hourly Continuation — CFX/USDT P8_144

**Symbol:** CFX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.9136 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.0923 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -0.5007 |
| sortino_ratio | -0.1305 |
| max_drawdown | 0.2707 |
| cagr | -0.0616 |
| net_avg_win | 90.7922 |
| net_avg_loss | -109.5690 |
| avg_hold_time_bars | 50.1067 |
| exposure | 0.7470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
