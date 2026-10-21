# EMA Hourly Continuation — KAVA/USDT P20_144

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.7033 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -2.3659 |
| sortino_ratio | -0.6674 |
| max_drawdown | 0.5613 |
| cagr | -0.2687 |
| net_avg_win | 68.2639 |
| net_avg_loss | -88.6236 |
| avg_hold_time_bars | 31.3081 |
| exposure | 0.5635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
