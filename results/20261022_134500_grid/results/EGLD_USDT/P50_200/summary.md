# EMA Hourly Continuation — EGLD/USDT P50_200

**Symbol:** EGLD/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.5955 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.9213 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -2.7679 |
| sortino_ratio | -0.7393 |
| max_drawdown | 0.5965 |
| cagr | -0.2948 |
| net_avg_win | 51.8016 |
| net_avg_loss | -75.6008 |
| avg_hold_time_bars | 25.7311 |
| exposure | 0.4175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
