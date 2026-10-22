# EMA Hourly Continuation — ACE/USDT P20_55

**Symbol:** ACE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.7529 |
| net_win_rate | 0.5112 |
| gross_profit_factor | 1.0122 |
| gross_win_rate | 0.5112 |
| sharpe_ratio | -1.8399 |
| sortino_ratio | -0.6113 |
| max_drawdown | 0.5485 |
| cagr | -0.2443 |
| net_avg_win | 56.1214 |
| net_avg_loss | -77.9458 |
| avg_hold_time_bars | 9.5409 |
| exposure | 0.2323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
