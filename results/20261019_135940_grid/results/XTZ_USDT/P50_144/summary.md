# EMA Hourly Continuation — XTZ/USDT P50_144

**Symbol:** XTZ/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.6420 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 1.0576 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.4585 |
| sortino_ratio | -1.1014 |
| max_drawdown | 0.7459 |
| cagr | -0.4080 |
| net_avg_win | 52.9223 |
| net_avg_loss | -78.6299 |
| avg_hold_time_bars | 13.1654 |
| exposure | 0.3040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
