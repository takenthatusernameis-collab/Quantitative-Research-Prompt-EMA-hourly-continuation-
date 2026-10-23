# EMA Hourly Continuation — CELR/USDT P34_200

**Symbol:** CELR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7048 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9302 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.1798 |
| sortino_ratio | -0.5954 |
| max_drawdown | 0.5330 |
| cagr | -0.2420 |
| net_avg_win | 67.8431 |
| net_avg_loss | -86.9243 |
| avg_hold_time_bars | 31.8177 |
| exposure | 0.5370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
