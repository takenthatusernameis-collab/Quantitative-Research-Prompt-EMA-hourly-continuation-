# EMA Hourly Continuation — ROSE/USDT P20_89

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 748 |
| net_profit_factor | 0.6535 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.9279 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -4.2753 |
| sortino_ratio | -1.6484 |
| max_drawdown | 0.8708 |
| cagr | -0.5428 |
| net_avg_win | 46.7286 |
| net_avg_loss | -61.8794 |
| avg_hold_time_bars | 12.0749 |
| exposure | 0.4105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
