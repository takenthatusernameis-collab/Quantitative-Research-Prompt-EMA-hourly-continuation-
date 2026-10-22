# EMA Hourly Continuation — SUPER/USDT P26_50

**Symbol:** SUPER/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 946 |
| net_profit_factor | 0.4732 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8153 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -6.7636 |
| sortino_ratio | -2.9487 |
| max_drawdown | 0.9720 |
| cagr | -0.7564 |
| net_avg_win | 20.3318 |
| net_avg_loss | -35.6557 |
| avg_hold_time_bars | 4.2622 |
| exposure | 0.1833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
