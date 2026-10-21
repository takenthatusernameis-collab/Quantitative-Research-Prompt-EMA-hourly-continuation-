# EMA Hourly Continuation — INJ/USDT P55_200

**Symbol:** INJ/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.6862 |
| net_win_rate | 0.4513 |
| gross_profit_factor | 0.8091 |
| gross_win_rate | 0.4513 |
| sharpe_ratio | -1.8599 |
| sortino_ratio | -0.4384 |
| max_drawdown | 0.4119 |
| cagr | -0.1829 |
| net_avg_win | 69.5962 |
| net_avg_loss | -83.4055 |
| avg_hold_time_bars | 25.3105 |
| exposure | 0.3187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
