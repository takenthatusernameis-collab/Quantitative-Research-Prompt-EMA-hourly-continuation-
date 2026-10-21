# EMA Hourly Continuation — API3/USDT P20_144

**Symbol:** API3/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.7867 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9456 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.5599 |
| sortino_ratio | -0.4544 |
| max_drawdown | 0.4597 |
| cagr | -0.1895 |
| net_avg_win | 74.4890 |
| net_avg_loss | -89.8200 |
| avg_hold_time_bars | 28.4652 |
| exposure | 0.5395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
