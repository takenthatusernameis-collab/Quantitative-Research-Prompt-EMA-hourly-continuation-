# EMA Hourly Continuation — AIOZ/USDT P21_34

**Symbol:** AIOZ/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1206 |
| net_profit_factor | 0.4533 |
| net_win_rate | 0.4088 |
| gross_profit_factor | 0.8408 |
| gross_win_rate | 0.4353 |
| sharpe_ratio | -10.6086 |
| sortino_ratio | -5.1919 |
| max_drawdown | 0.9987 |
| cagr | -0.9280 |
| net_avg_win | 16.7970 |
| net_avg_loss | -25.6205 |
| avg_hold_time_bars | 2.6708 |
| exposure | 0.1464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
