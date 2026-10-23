# EMA Hourly Continuation — ORDI/USDT P89_144

**Symbol:** ORDI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.5167 |
| net_win_rate | 0.4483 |
| gross_profit_factor | 0.8429 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -4.4991 |
| sortino_ratio | -1.4519 |
| max_drawdown | 0.8284 |
| cagr | -0.5013 |
| net_avg_win | 37.7246 |
| net_avg_loss | -59.3219 |
| avg_hold_time_bars | 4.7720 |
| exposure | 0.1132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
