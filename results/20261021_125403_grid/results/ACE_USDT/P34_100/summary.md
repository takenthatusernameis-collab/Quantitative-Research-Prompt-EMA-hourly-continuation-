# EMA Hourly Continuation — ACE/USDT P34_100

**Symbol:** ACE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.8321 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0753 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -1.1582 |
| sortino_ratio | -0.3353 |
| max_drawdown | 0.3700 |
| cagr | -0.1443 |
| net_avg_win | 76.3678 |
| net_avg_loss | -98.2980 |
| avg_hold_time_bars | 14.6495 |
| exposure | 0.2705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
