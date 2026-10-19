# EMA Hourly Continuation — PEPE/USDT P21_144

**Symbol:** PEPE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.5803 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8557 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -3.5018 |
| sortino_ratio | -1.0211 |
| max_drawdown | 0.7073 |
| cagr | -0.3869 |
| net_avg_win | 49.6529 |
| net_avg_loss | -71.7231 |
| avg_hold_time_bars | 29.1736 |
| exposure | 0.5729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
