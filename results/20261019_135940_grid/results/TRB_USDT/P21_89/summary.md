# EMA Hourly Continuation — TRB/USDT P21_89

**Symbol:** TRB/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.4294 |
| net_win_rate | 0.4061 |
| gross_profit_factor | 0.7133 |
| gross_win_rate | 0.4284 |
| sharpe_ratio | -6.8401 |
| sortino_ratio | -2.5729 |
| max_drawdown | 0.9588 |
| cagr | -0.7143 |
| net_avg_win | 24.6741 |
| net_avg_loss | -39.2990 |
| avg_hold_time_bars | 12.4242 |
| exposure | 0.4042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
