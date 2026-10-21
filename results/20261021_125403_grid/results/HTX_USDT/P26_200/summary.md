# EMA Hourly Continuation — HTX/USDT P26_200

**Symbol:** HTX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.6130 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.9054 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -2.8794 |
| sortino_ratio | -0.6802 |
| max_drawdown | 0.5911 |
| cagr | -0.2746 |
| net_avg_win | 68.6990 |
| net_avg_loss | -96.9201 |
| avg_hold_time_bars | 47.1486 |
| exposure | 0.5889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
