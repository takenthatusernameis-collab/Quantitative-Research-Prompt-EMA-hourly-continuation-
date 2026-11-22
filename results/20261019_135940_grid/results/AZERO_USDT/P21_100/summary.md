# EMA Hourly Continuation — AZERO/USDT P21_100

**Symbol:** AZERO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.6287 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.9693 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -3.7795 |
| sortino_ratio | -1.3021 |
| max_drawdown | 0.8167 |
| cagr | -0.4742 |
| net_avg_win | 46.6808 |
| net_avg_loss | -65.6775 |
| avg_hold_time_bars | 15.0403 |
| exposure | 0.4220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
