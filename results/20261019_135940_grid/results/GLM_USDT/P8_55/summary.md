# EMA Hourly Continuation — GLM/USDT P8_55

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 969 |
| net_profit_factor | 0.4792 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.7868 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -6.1574 |
| sortino_ratio | -2.7012 |
| max_drawdown | 0.9625 |
| cagr | -0.7261 |
| net_avg_win | 20.1909 |
| net_avg_loss | -34.7582 |
| avg_hold_time_bars | 11.7410 |
| exposure | 0.5171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
