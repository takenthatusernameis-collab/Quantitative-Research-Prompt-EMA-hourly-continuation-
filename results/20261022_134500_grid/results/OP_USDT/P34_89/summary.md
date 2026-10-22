# EMA Hourly Continuation — OP/USDT P34_89

**Symbol:** OP/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.5848 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9121 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -4.2842 |
| sortino_ratio | -1.5819 |
| max_drawdown | 0.8582 |
| cagr | -0.5292 |
| net_avg_win | 36.6940 |
| net_avg_loss | -56.9750 |
| avg_hold_time_bars | 8.0934 |
| exposure | 0.2520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
