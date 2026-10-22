# EMA Hourly Continuation — CWEB/USDT P26_89

**Symbol:** CWEB/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.4756 |
| net_win_rate | 0.3947 |
| gross_profit_factor | 0.7865 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -6.8817 |
| sortino_ratio | -2.2990 |
| max_drawdown | 0.9487 |
| cagr | -0.6903 |
| net_avg_win | 38.1909 |
| net_avg_loss | -52.3657 |
| avg_hold_time_bars | 14.2456 |
| exposure | 0.3691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
