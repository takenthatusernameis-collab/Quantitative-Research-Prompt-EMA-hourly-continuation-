# EMA Hourly Continuation — COTI/USDT P55_100

**Symbol:** COTI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.8511 |
| net_win_rate | 0.5311 |
| gross_profit_factor | 1.1082 |
| gross_win_rate | 0.5311 |
| sharpe_ratio | -0.7802 |
| sortino_ratio | -0.2023 |
| max_drawdown | 0.2954 |
| cagr | -0.0905 |
| net_avg_win | 70.8513 |
| net_avg_loss | -94.2724 |
| avg_hold_time_bars | 8.0031 |
| exposure | 0.1171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
