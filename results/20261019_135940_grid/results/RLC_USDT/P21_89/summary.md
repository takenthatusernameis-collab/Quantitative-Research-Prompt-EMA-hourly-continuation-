# EMA Hourly Continuation — RLC/USDT P21_89

**Symbol:** RLC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 754 |
| net_profit_factor | 0.6617 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 1.0270 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -3.8193 |
| sortino_ratio | -1.4800 |
| max_drawdown | 0.8433 |
| cagr | -0.5064 |
| net_avg_win | 43.5290 |
| net_avg_loss | -64.4057 |
| avg_hold_time_bars | 10.0928 |
| exposure | 0.3459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
