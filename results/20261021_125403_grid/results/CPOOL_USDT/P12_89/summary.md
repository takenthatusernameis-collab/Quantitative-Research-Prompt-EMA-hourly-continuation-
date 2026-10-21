# EMA Hourly Continuation — CPOOL/USDT P12_89

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.8757 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0223 |
| gross_win_rate | 0.5071 |
| sharpe_ratio | -0.9767 |
| sortino_ratio | -0.3329 |
| max_drawdown | 0.3919 |
| cagr | -0.1463 |
| net_avg_win | 80.4608 |
| net_avg_loss | -94.5185 |
| avg_hold_time_bars | 17.3251 |
| exposure | 0.4457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
