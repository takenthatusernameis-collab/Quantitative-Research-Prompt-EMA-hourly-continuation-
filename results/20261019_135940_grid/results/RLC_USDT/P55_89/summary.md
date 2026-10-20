# EMA Hourly Continuation — RLC/USDT P55_89

**Symbol:** RLC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.4683 |
| net_win_rate | 0.4619 |
| gross_profit_factor | 0.9058 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -5.8840 |
| sortino_ratio | -2.1757 |
| max_drawdown | 0.9349 |
| cagr | -0.6521 |
| net_avg_win | 25.9912 |
| net_avg_loss | -47.6340 |
| avg_hold_time_bars | 4.5557 |
| exposure | 0.1412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
