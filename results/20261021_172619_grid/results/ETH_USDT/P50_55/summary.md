# EMA Hourly Continuation — ETH/USDT P50_55

**Symbol:** ETH/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 80 |
| net_profit_factor | 0.6654 |
| net_win_rate | 0.5250 |
| gross_profit_factor | 1.0933 |
| gross_win_rate | 0.5250 |
| sharpe_ratio | -1.0661 |
| sortino_ratio | -0.1379 |
| max_drawdown | 0.1650 |
| cagr | -0.0602 |
| net_avg_win | 68.3824 |
| net_avg_loss | -113.5878 |
| avg_hold_time_bars | 6.2750 |
| exposure | 0.0228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
