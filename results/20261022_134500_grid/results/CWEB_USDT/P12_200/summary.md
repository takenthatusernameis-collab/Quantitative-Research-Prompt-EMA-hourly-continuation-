# EMA Hourly Continuation — CWEB/USDT P12_200

**Symbol:** CWEB/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.7538 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 1.0261 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.5490 |
| sortino_ratio | -0.3423 |
| max_drawdown | 0.4152 |
| cagr | -0.1508 |
| net_avg_win | 84.4629 |
| net_avg_loss | -111.1459 |
| avg_hold_time_bars | 71.4980 |
| exposure | 0.7962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
