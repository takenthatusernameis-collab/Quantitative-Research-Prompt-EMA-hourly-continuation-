# EMA Hourly Continuation — KSM/USDT P26_89

**Symbol:** KSM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.5597 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9139 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -4.9086 |
| sortino_ratio | -1.7730 |
| max_drawdown | 0.8942 |
| cagr | -0.5812 |
| net_avg_win | 35.9371 |
| net_avg_loss | -57.1114 |
| avg_hold_time_bars | 10.6297 |
| exposure | 0.3223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
