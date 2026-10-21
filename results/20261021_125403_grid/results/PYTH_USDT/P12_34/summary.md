# EMA Hourly Continuation — PYTH/USDT P12_34

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 581 |
| net_profit_factor | 0.7980 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0237 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -1.8337 |
| sortino_ratio | -0.6337 |
| max_drawdown | 0.5771 |
| cagr | -0.2531 |
| net_avg_win | 70.2968 |
| net_avg_loss | -89.0009 |
| avg_hold_time_bars | 6.4200 |
| exposure | 0.1695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
