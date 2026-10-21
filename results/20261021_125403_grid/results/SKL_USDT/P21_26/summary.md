# EMA Hourly Continuation — SKL/USDT P21_26

**Symbol:** SKL/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 198 |
| net_profit_factor | 0.5956 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.8653 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -2.2573 |
| sortino_ratio | -0.4547 |
| max_drawdown | 0.4320 |
| cagr | -0.1878 |
| net_avg_win | 65.1641 |
| net_avg_loss | -94.9509 |
| avg_hold_time_bars | 4.3232 |
| exposure | 0.0389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
