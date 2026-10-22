# EMA Hourly Continuation — XAI/USDT P8_12

**Symbol:** XAI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.6717 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9234 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -2.4273 |
| sortino_ratio | -0.6501 |
| max_drawdown | 0.5448 |
| cagr | -0.2573 |
| net_avg_win | 64.0760 |
| net_avg_loss | -88.0564 |
| avg_hold_time_bars | 4.3971 |
| exposure | 0.0700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
