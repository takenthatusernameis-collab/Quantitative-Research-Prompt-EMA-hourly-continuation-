# EMA Hourly Continuation — ZETA/USDT P34_89

**Symbol:** ZETA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.6406 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.9841 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -5.1017 |
| sortino_ratio | -1.8903 |
| max_drawdown | 0.9103 |
| cagr | -0.6038 |
| net_avg_win | 49.8452 |
| net_avg_loss | -66.1372 |
| avg_hold_time_bars | 7.7055 |
| exposure | 0.2451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
