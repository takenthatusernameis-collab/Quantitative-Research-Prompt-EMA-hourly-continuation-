# EMA Hourly Continuation — SSV/USDT P12_21

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1553 |
| net_profit_factor | 0.4267 |
| net_win_rate | 0.4153 |
| gross_profit_factor | 0.8949 |
| gross_win_rate | 0.4424 |
| sharpe_ratio | -12.3189 |
| sortino_ratio | -6.8470 |
| max_drawdown | 0.9998 |
| cagr | -0.9692 |
| net_avg_win | 11.5392 |
| net_avg_loss | -19.2084 |
| avg_hold_time_bars | 2.4816 |
| exposure | 0.1744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
