# EMA Hourly Continuation — CPOOL/USDT P12_200

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.7827 |
| net_win_rate | 0.4692 |
| gross_profit_factor | 0.8755 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -1.5136 |
| sortino_ratio | -0.4236 |
| max_drawdown | 0.4263 |
| cagr | -0.1789 |
| net_avg_win | 76.8721 |
| net_avg_loss | -86.8252 |
| avg_hold_time_bars | 36.8282 |
| exposure | 0.6529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
