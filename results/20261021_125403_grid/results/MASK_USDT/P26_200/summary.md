# EMA Hourly Continuation — MASK/USDT P26_200

**Symbol:** MASK/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7176 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9229 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.7500 |
| sortino_ratio | -0.4586 |
| max_drawdown | 0.4282 |
| cagr | -0.1906 |
| net_avg_win | 63.8533 |
| net_avg_loss | -84.3486 |
| avg_hold_time_bars | 35.4451 |
| exposure | 0.5430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
