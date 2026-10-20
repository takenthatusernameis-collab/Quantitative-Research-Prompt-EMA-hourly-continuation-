# EMA Hourly Continuation — MEW/USDT P21_200

**Symbol:** MEW/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.7238 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9358 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -1.9548 |
| sortino_ratio | -0.5375 |
| max_drawdown | 0.5346 |
| cagr | -0.2232 |
| net_avg_win | 67.6202 |
| net_avg_loss | -87.1943 |
| avg_hold_time_bars | 36.7321 |
| exposure | 0.6295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
