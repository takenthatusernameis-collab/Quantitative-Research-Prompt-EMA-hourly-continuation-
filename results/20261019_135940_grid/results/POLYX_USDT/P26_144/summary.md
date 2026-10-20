# EMA Hourly Continuation — POLYX/USDT P26_144

**Symbol:** POLYX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7152 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 1.0428 |
| gross_win_rate | 0.5144 |
| sharpe_ratio | -2.2350 |
| sortino_ratio | -0.6975 |
| max_drawdown | 0.5898 |
| cagr | -0.2804 |
| net_avg_win | 57.8662 |
| net_avg_loss | -81.5819 |
| avg_hold_time_bars | 21.5288 |
| exposure | 0.4756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
