# EMA Hourly Continuation — MINA/USDT P21_100

**Symbol:** MINA/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.8806 |
| net_win_rate | 0.5291 |
| gross_profit_factor | 1.0952 |
| gross_win_rate | 0.5291 |
| sharpe_ratio | -0.7148 |
| sortino_ratio | -0.2174 |
| max_drawdown | 0.3846 |
| cagr | -0.0993 |
| net_avg_win | 72.2035 |
| net_avg_loss | -92.1451 |
| avg_hold_time_bars | 22.9619 |
| exposure | 0.4655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
