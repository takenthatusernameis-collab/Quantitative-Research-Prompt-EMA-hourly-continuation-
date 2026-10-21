# EMA Hourly Continuation — MLK/USDT P12_144

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.5601 |
| net_win_rate | 0.3991 |
| gross_profit_factor | 0.7005 |
| gross_win_rate | 0.3991 |
| sharpe_ratio | -4.1986 |
| sortino_ratio | -1.2662 |
| max_drawdown | 0.7726 |
| cagr | -0.4441 |
| net_avg_win | 53.4590 |
| net_avg_loss | -63.4009 |
| avg_hold_time_bars | 26.4425 |
| exposure | 0.5517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
