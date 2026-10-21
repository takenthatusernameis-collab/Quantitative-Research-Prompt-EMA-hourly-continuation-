# EMA Hourly Continuation — FIDA/USDT P34_89

**Symbol:** FIDA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.6871 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9119 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -2.4969 |
| sortino_ratio | -0.7815 |
| max_drawdown | 0.6105 |
| cagr | -0.3009 |
| net_avg_win | 56.2876 |
| net_avg_loss | -75.7180 |
| avg_hold_time_bars | 10.9834 |
| exposure | 0.2401 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
