# EMA Hourly Continuation — SUPER/USDT P12_26

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.7700 |
| net_win_rate | 0.5182 |
| gross_profit_factor | 1.0858 |
| gross_win_rate | 0.5239 |
| sharpe_ratio | -1.9687 |
| sortino_ratio | -0.6467 |
| max_drawdown | 0.5674 |
| cagr | -0.2581 |
| net_avg_win | 65.1660 |
| net_avg_loss | -91.0115 |
| avg_hold_time_bars | 5.0841 |
| exposure | 0.1209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
