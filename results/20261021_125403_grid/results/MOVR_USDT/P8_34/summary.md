# EMA Hourly Continuation — MOVR/USDT P8_34

**Symbol:** MOVR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 841 |
| net_profit_factor | 0.7339 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9693 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -2.6849 |
| sortino_ratio | -1.1154 |
| max_drawdown | 0.7407 |
| cagr | -0.4004 |
| net_avg_win | 47.8285 |
| net_avg_loss | -64.0964 |
| avg_hold_time_bars | 8.0797 |
| exposure | 0.3089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
