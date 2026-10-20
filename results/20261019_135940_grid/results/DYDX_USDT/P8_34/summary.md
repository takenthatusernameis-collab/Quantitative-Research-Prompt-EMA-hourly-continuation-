# EMA Hourly Continuation — DYDX/USDT P8_34

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1302 |
| net_profit_factor | 0.5884 |
| net_win_rate | 0.4578 |
| gross_profit_factor | 1.0485 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -7.4735 |
| sortino_ratio | -3.7781 |
| max_drawdown | 0.9906 |
| cagr | -0.8417 |
| net_avg_win | 23.7563 |
| net_avg_loss | -34.0810 |
| avg_hold_time_bars | 6.2796 |
| exposure | 0.3716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
