# EMA Hourly Continuation — BTT/USDT P34_144

**Symbol:** BTT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.4369 |
| net_win_rate | 0.3953 |
| gross_profit_factor | 0.8595 |
| gross_win_rate | 0.4372 |
| sharpe_ratio | -6.4572 |
| sortino_ratio | -1.8991 |
| max_drawdown | 0.9110 |
| cagr | -0.6184 |
| net_avg_win | 41.5738 |
| net_avg_loss | -62.2218 |
| avg_hold_time_bars | 23.8302 |
| exposure | 0.4658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
