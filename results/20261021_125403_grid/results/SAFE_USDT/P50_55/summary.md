# EMA Hourly Continuation — SAFE/USDT P50_55

**Symbol:** SAFE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 137 |
| net_profit_factor | 0.6442 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9264 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -1.5755 |
| sortino_ratio | -0.2651 |
| max_drawdown | 0.2952 |
| cagr | -0.1136 |
| net_avg_win | 71.2128 |
| net_avg_loss | -102.7524 |
| avg_hold_time_bars | 8.9197 |
| exposure | 0.0560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
