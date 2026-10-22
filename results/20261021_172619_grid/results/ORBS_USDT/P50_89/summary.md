# EMA Hourly Continuation — ORBS/USDT P50_89

**Symbol:** ORBS/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.6469 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9838 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -3.2371 |
| sortino_ratio | -0.9139 |
| max_drawdown | 0.6706 |
| cagr | -0.3430 |
| net_avg_win | 64.8996 |
| net_avg_loss | -90.4880 |
| avg_hold_time_bars | 8.6778 |
| exposure | 0.1530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
