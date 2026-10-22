# EMA Hourly Continuation — ENA/USDT P34_144

**Symbol:** ENA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.6986 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9284 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -2.1485 |
| sortino_ratio | -0.6627 |
| max_drawdown | 0.5686 |
| cagr | -0.2680 |
| net_avg_win | 54.2680 |
| net_avg_loss | -73.8578 |
| avg_hold_time_bars | 17.2983 |
| exposure | 0.3743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
