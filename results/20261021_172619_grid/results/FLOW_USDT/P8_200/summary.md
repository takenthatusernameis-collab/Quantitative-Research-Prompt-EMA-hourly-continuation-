# EMA Hourly Continuation — FLOW/USDT P8_200

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.7670 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9106 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -1.3654 |
| sortino_ratio | -0.3178 |
| max_drawdown | 0.3235 |
| cagr | -0.1369 |
| net_avg_win | 79.4948 |
| net_avg_loss | -94.7603 |
| avg_hold_time_bars | 66.8433 |
| exposure | 0.8143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
