# EMA Hourly Continuation — BRETT/USDT P26_34

**Symbol:** BRETT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 176 |
| net_profit_factor | 0.8880 |
| net_win_rate | 0.5341 |
| gross_profit_factor | 1.1359 |
| gross_win_rate | 0.5341 |
| sharpe_ratio | -0.4707 |
| sortino_ratio | -0.0929 |
| max_drawdown | 0.1703 |
| cagr | -0.0433 |
| net_avg_win | 84.0431 |
| net_avg_loss | -108.4907 |
| avg_hold_time_bars | 5.5966 |
| exposure | 0.0474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
