# EMA Hourly Continuation — ETHFI/USDT P20_21

**Symbol:** ETHFI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1253 |
| net_profit_factor | 0.2278 |
| net_win_rate | 0.3113 |
| gross_profit_factor | 0.7692 |
| gross_win_rate | 0.3583 |
| sharpe_ratio | -17.1810 |
| sortino_ratio | -9.0341 |
| max_drawdown | 1.0000 |
| cagr | -0.9939 |
| net_avg_win | 7.5656 |
| net_avg_loss | -15.0064 |
| avg_hold_time_bars | 1.8061 |
| exposure | 0.1029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
