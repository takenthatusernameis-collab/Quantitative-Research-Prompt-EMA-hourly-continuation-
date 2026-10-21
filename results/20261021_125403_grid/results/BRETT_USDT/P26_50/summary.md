# EMA Hourly Continuation — BRETT/USDT P26_50

**Symbol:** BRETT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7210 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.8936 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -1.9157 |
| sortino_ratio | -0.5324 |
| max_drawdown | 0.4501 |
| cagr | -0.2173 |
| net_avg_win | 66.5896 |
| net_avg_loss | -84.0116 |
| avg_hold_time_bars | 6.8830 |
| exposure | 0.1189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
