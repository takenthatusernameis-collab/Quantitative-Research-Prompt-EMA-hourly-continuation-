# EMA Hourly Continuation — SUSHI/USDT P26_89

**Symbol:** SUSHI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.7401 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9387 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -2.0882 |
| sortino_ratio | -0.6543 |
| max_drawdown | 0.5604 |
| cagr | -0.2599 |
| net_avg_win | 64.7392 |
| net_avg_loss | -82.2022 |
| avg_hold_time_bars | 14.3830 |
| exposure | 0.3144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
