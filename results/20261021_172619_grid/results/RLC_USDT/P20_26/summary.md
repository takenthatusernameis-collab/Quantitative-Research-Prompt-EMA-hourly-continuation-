# EMA Hourly Continuation — RLC/USDT P20_26

**Symbol:** RLC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.5408 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8337 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -3.3389 |
| sortino_ratio | -0.8362 |
| max_drawdown | 0.6355 |
| cagr | -0.3196 |
| net_avg_win | 52.5110 |
| net_avg_loss | -81.3076 |
| avg_hold_time_bars | 4.6525 |
| exposure | 0.0645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
