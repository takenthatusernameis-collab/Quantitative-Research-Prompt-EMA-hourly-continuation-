# EMA Hourly Continuation — ADA/USDT P12_100

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.7928 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9918 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -1.6427 |
| sortino_ratio | -0.5116 |
| max_drawdown | 0.4795 |
| cagr | -0.2104 |
| net_avg_win | 72.8437 |
| net_avg_loss | -90.3444 |
| avg_hold_time_bars | 25.1624 |
| exposure | 0.5421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
