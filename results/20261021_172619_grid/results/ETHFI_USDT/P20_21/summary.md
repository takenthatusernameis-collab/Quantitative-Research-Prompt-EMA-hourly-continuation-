# EMA Hourly Continuation — ETHFI/USDT P20_21

**Symbol:** ETHFI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 126 |
| net_profit_factor | 0.7712 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9666 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -0.9106 |
| sortino_ratio | -0.1463 |
| max_drawdown | 0.1754 |
| cagr | -0.0654 |
| net_avg_win | 84.9246 |
| net_avg_loss | -106.6724 |
| avg_hold_time_bars | 6.8016 |
| exposure | 0.0390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
