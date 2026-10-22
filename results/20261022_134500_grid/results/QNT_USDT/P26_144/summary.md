# EMA Hourly Continuation — QNT/USDT P26_144

**Symbol:** QNT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.5601 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9326 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -4.1591 |
| sortino_ratio | -1.5051 |
| max_drawdown | 0.8481 |
| cagr | -0.5134 |
| net_avg_win | 33.8057 |
| net_avg_loss | -55.1033 |
| avg_hold_time_bars | 14.6061 |
| exposure | 0.4382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
