# EMA Hourly Continuation — VELO/USDT P20_200

**Symbol:** VELO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.9855 |
| net_win_rate | 0.5312 |
| gross_profit_factor | 1.1182 |
| gross_win_rate | 0.5312 |
| sharpe_ratio | -0.0225 |
| sortino_ratio | -0.0060 |
| max_drawdown | 0.2037 |
| cagr | -0.0093 |
| net_avg_win | 87.6160 |
| net_avg_loss | -100.7220 |
| avg_hold_time_bars | 40.1187 |
| exposure | 0.6145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
