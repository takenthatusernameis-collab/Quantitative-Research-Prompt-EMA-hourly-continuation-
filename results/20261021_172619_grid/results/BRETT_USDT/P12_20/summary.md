# EMA Hourly Continuation — BRETT/USDT P12_20

**Symbol:** BRETT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.7762 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 0.9915 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -1.3546 |
| sortino_ratio | -0.3275 |
| max_drawdown | 0.3409 |
| cagr | -0.1399 |
| net_avg_win | 77.8038 |
| net_avg_loss | -99.4985 |
| avg_hold_time_bars | 5.2974 |
| exposure | 0.0686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
