# EMA Hourly Continuation — AIOZ/USDT P21_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.8999 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -2.9034 |
| sortino_ratio | -0.8893 |
| max_drawdown | 0.6990 |
| cagr | -0.3415 |
| net_avg_win | 57.7650 |
| net_avg_loss | -78.8647 |
| avg_hold_time_bars | 28.8865 |
| exposure | 0.6132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
