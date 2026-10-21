# EMA Hourly Continuation — NEAR/USDT P12_200

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.9444 |
| net_win_rate | 0.5192 |
| gross_profit_factor | 1.0726 |
| gross_win_rate | 0.5192 |
| sharpe_ratio | -0.2588 |
| sortino_ratio | -0.0600 |
| max_drawdown | 0.2692 |
| cagr | -0.0311 |
| net_avg_win | 95.9106 |
| net_avg_loss | -109.6790 |
| avg_hold_time_bars | 63.9538 |
| exposure | 0.7558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
