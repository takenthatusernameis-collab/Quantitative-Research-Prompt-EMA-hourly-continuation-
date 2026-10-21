# EMA Hourly Continuation — NEAR/USDT P144_200

**Symbol:** NEAR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 188 |
| net_profit_factor | 0.8449 |
| net_win_rate | 0.5266 |
| gross_profit_factor | 1.1035 |
| gross_win_rate | 0.5266 |
| sharpe_ratio | -0.6931 |
| sortino_ratio | -0.1371 |
| max_drawdown | 0.2199 |
| cagr | -0.0619 |
| net_avg_win | 81.6500 |
| net_avg_loss | -107.4930 |
| avg_hold_time_bars | 7.0266 |
| exposure | 0.0600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
