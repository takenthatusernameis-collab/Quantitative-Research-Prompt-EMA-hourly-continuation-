# EMA Hourly Continuation — TIA/USDT P50_100

**Symbol:** TIA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.6779 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9980 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -3.0987 |
| sortino_ratio | -1.0458 |
| max_drawdown | 0.7152 |
| cagr | -0.3919 |
| net_avg_win | 53.4158 |
| net_avg_loss | -76.6165 |
| avg_hold_time_bars | 6.6439 |
| exposure | 0.1721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
