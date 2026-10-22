# EMA Hourly Continuation — OSMO/USDT P34_200

**Symbol:** OSMO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.9067 |
| net_win_rate | 0.5272 |
| gross_profit_factor | 1.1084 |
| gross_win_rate | 0.5272 |
| sharpe_ratio | -0.5071 |
| sortino_ratio | -0.1252 |
| max_drawdown | 0.2622 |
| cagr | -0.0593 |
| net_avg_win | 89.3037 |
| net_avg_loss | -109.8285 |
| avg_hold_time_bars | 37.7857 |
| exposure | 0.5050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
