# EMA Hourly Continuation — PYTH/USDT P21_34

**Symbol:** PYTH/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.6691 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.8903 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -2.3906 |
| sortino_ratio | -0.6013 |
| max_drawdown | 0.5201 |
| cagr | -0.2405 |
| net_avg_win | 70.0335 |
| net_avg_loss | -90.2544 |
| avg_hold_time_bars | 4.5209 |
| exposure | 0.0639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
