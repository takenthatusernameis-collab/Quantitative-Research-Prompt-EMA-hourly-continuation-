# EMA Hourly Continuation — TAIKO/USDT P12_89

**Symbol:** TAIKO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.6322 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9450 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -3.7668 |
| sortino_ratio | -1.3868 |
| max_drawdown | 0.8165 |
| cagr | -0.4902 |
| net_avg_win | 43.0073 |
| net_avg_loss | -64.0192 |
| avg_hold_time_bars | 16.9802 |
| exposure | 0.5367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
