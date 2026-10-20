# EMA Hourly Continuation — ROSE/USDT P21_89

**Symbol:** ROSE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 748 |
| net_profit_factor | 0.6699 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9605 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -3.9675 |
| sortino_ratio | -1.5312 |
| max_drawdown | 0.8509 |
| cagr | -0.5160 |
| net_avg_win | 47.9228 |
| net_avg_loss | -64.6207 |
| avg_hold_time_bars | 11.5989 |
| exposure | 0.3944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
