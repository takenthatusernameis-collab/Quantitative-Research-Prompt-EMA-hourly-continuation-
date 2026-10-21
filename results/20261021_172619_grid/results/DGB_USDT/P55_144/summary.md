# EMA Hourly Continuation — DGB/USDT P55_144

**Symbol:** DGB/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7232 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9187 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -1.9421 |
| sortino_ratio | -0.5168 |
| max_drawdown | 0.4492 |
| cagr | -0.2114 |
| net_avg_win | 70.7139 |
| net_avg_loss | -89.1813 |
| avg_hold_time_bars | 15.6753 |
| exposure | 0.2480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
