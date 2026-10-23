# EMA Hourly Continuation — WEMIX/USDT P55_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.3368 |
| net_win_rate | 0.3129 |
| gross_profit_factor | 0.5282 |
| gross_win_rate | 0.3221 |
| sharpe_ratio | -9.4864 |
| sortino_ratio | -3.4163 |
| max_drawdown | 0.9867 |
| cagr | -0.8204 |
| net_avg_win | 24.5656 |
| net_avg_loss | -33.2081 |
| avg_hold_time_bars | 13.1764 |
| exposure | 0.3905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
