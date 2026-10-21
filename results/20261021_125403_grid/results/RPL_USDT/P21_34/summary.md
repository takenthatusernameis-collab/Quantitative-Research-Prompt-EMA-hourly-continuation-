# EMA Hourly Continuation — RPL/USDT P21_34

**Symbol:** RPL/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 510 |
| net_profit_factor | 0.5945 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.8653 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -4.2290 |
| sortino_ratio | -1.3604 |
| max_drawdown | 0.7950 |
| cagr | -0.4665 |
| net_avg_win | 51.3536 |
| net_avg_loss | -69.2845 |
| avg_hold_time_bars | 5.9157 |
| exposure | 0.1365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
