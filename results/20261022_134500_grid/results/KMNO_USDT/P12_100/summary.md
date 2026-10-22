# EMA Hourly Continuation — KMNO/USDT P12_100

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.6470 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.9038 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -3.2940 |
| sortino_ratio | -1.0578 |
| max_drawdown | 0.7148 |
| cagr | -0.3980 |
| net_avg_win | 54.6007 |
| net_avg_loss | -73.1140 |
| avg_hold_time_bars | 24.5803 |
| exposure | 0.5867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
