# EMA Hourly Continuation — MANTA/USDT P8_200

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.8072 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9399 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -1.1095 |
| sortino_ratio | -0.2454 |
| max_drawdown | 0.3291 |
| cagr | -0.1074 |
| net_avg_win | 89.5971 |
| net_avg_loss | -103.0015 |
| avg_hold_time_bars | 76.2531 |
| exposure | 0.8353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
