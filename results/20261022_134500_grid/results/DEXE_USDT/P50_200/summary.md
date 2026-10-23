# EMA Hourly Continuation — DEXE/USDT P50_200

**Symbol:** DEXE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.8058 |
| net_win_rate | 0.5256 |
| gross_profit_factor | 1.0964 |
| gross_win_rate | 0.5324 |
| sharpe_ratio | -0.9900 |
| sortino_ratio | -0.2405 |
| max_drawdown | 0.3743 |
| cagr | -0.1092 |
| net_avg_win | 67.8811 |
| net_avg_loss | -93.3333 |
| avg_hold_time_bars | 39.5392 |
| exposure | 0.5266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
