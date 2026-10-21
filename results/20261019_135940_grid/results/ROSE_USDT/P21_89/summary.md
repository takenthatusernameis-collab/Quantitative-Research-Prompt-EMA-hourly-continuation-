# EMA Hourly Continuation — ROSE/USDT P21_89

**Symbol:** ROSE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.6672 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.9557 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -3.9784 |
| sortino_ratio | -1.5322 |
| max_drawdown | 0.8509 |
| cagr | -0.5163 |
| net_avg_win | 47.6241 |
| net_avg_loss | -64.2798 |
| avg_hold_time_bars | 11.6644 |
| exposure | 0.3950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
