# EMA Hourly Continuation — EUL/USDT P34_144

**Symbol:** EUL/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.5391 |
| net_win_rate | 0.4467 |
| gross_profit_factor | 0.7534 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -3.5813 |
| sortino_ratio | -1.1136 |
| max_drawdown | 0.7446 |
| cagr | -0.4086 |
| net_avg_win | 39.3171 |
| net_avg_loss | -58.8803 |
| avg_hold_time_bars | 15.9795 |
| exposure | 0.3545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
