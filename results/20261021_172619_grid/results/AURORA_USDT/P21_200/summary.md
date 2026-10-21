# EMA Hourly Continuation — AURORA/USDT P21_200

**Symbol:** AURORA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.6957 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8921 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -2.1844 |
| sortino_ratio | -0.5551 |
| max_drawdown | 0.4998 |
| cagr | -0.2260 |
| net_avg_win | 72.7955 |
| net_avg_loss | -91.1772 |
| avg_hold_time_bars | 38.1156 |
| exposure | 0.5544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
