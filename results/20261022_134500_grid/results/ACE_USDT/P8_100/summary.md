# EMA Hourly Continuation — ACE/USDT P8_100

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.7010 |
| net_win_rate | 0.4849 |
| gross_profit_factor | 0.9730 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -2.6511 |
| sortino_ratio | -0.8322 |
| max_drawdown | 0.6304 |
| cagr | -0.3227 |
| net_avg_win | 60.8730 |
| net_avg_loss | -81.7521 |
| avg_hold_time_bars | 29.8068 |
| exposure | 0.6704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
