# EMA Hourly Continuation — BIGTIME/USDT P8_34

**Symbol:** BIGTIME/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1225 |
| net_profit_factor | 0.6198 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9943 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -6.0860 |
| sortino_ratio | -3.0110 |
| max_drawdown | 0.9735 |
| cagr | -0.7590 |
| net_avg_win | 27.1863 |
| net_avg_loss | -39.8338 |
| avg_hold_time_bars | 6.6245 |
| exposure | 0.3672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
