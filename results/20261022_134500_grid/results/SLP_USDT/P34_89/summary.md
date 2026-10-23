# EMA Hourly Continuation — SLP/USDT P34_89

**Symbol:** SLP/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 793 |
| net_profit_factor | 0.6104 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.9962 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -5.2764 |
| sortino_ratio | -2.0838 |
| max_drawdown | 0.9241 |
| cagr | -0.6380 |
| net_avg_win | 38.7266 |
| net_avg_loss | -56.3468 |
| avg_hold_time_bars | 6.8689 |
| exposure | 0.2476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
