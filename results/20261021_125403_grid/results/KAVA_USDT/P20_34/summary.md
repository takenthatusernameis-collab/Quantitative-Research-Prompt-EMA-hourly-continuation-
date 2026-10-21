# EMA Hourly Continuation — KAVA/USDT P20_34

**Symbol:** KAVA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.5558 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.9242 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -4.2323 |
| sortino_ratio | -1.2444 |
| max_drawdown | 0.7771 |
| cagr | -0.4410 |
| net_avg_win | 49.5249 |
| net_avg_loss | -76.1517 |
| avg_hold_time_bars | 6.2423 |
| exposure | 0.1195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
