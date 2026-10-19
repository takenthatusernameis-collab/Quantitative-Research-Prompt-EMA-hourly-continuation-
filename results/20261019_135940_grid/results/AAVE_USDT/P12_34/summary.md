# EMA Hourly Continuation — AAVE/USDT P12_34

**Symbol:** AAVE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1305 |
| net_profit_factor | 0.4645 |
| net_win_rate | 0.4437 |
| gross_profit_factor | 0.8662 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -9.4062 |
| sortino_ratio | -4.7631 |
| max_drawdown | 0.9976 |
| cagr | -0.9090 |
| net_avg_win | 14.9432 |
| net_avg_loss | -25.6581 |
| avg_hold_time_bars | 3.8628 |
| exposure | 0.2291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
