# EMA Hourly Continuation — MLK/USDT P20_34

**Symbol:** MLK/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1454 |
| net_profit_factor | 0.1605 |
| net_win_rate | 0.2256 |
| gross_profit_factor | 0.5290 |
| gross_win_rate | 0.2545 |
| sharpe_ratio | -20.2329 |
| sortino_ratio | -11.4069 |
| max_drawdown | 1.0000 |
| cagr | -0.9975 |
| net_avg_win | 5.8305 |
| net_avg_loss | -10.5794 |
| avg_hold_time_bars | 2.7132 |
| exposure | 0.1785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
