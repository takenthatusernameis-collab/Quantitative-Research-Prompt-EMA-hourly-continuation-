# EMA Hourly Continuation — DUSK/USDT P12_34

**Symbol:** DUSK/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1271 |
| net_profit_factor | 0.6128 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 1.0705 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -7.3620 |
| sortino_ratio | -3.6899 |
| max_drawdown | 0.9890 |
| cagr | -0.8322 |
| net_avg_win | 27.0738 |
| net_avg_loss | -36.8480 |
| avg_hold_time_bars | 4.3619 |
| exposure | 0.2520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
