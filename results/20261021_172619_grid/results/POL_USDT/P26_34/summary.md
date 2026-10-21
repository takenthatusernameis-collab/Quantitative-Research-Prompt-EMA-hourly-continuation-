# EMA Hourly Continuation — POL/USDT P26_34

**Symbol:** POL/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 195 |
| net_profit_factor | 0.5507 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.7918 |
| gross_win_rate | 0.4462 |
| sharpe_ratio | -2.4987 |
| sortino_ratio | -0.4987 |
| max_drawdown | 0.4478 |
| cagr | -0.2049 |
| net_avg_win | 61.6657 |
| net_avg_loss | -90.2115 |
| avg_hold_time_bars | 5.8103 |
| exposure | 0.0515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
