# EMA Hourly Continuation — UMA/USDT P12_34

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1195 |
| net_profit_factor | 0.4100 |
| net_win_rate | 0.4251 |
| gross_profit_factor | 0.8380 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -9.4655 |
| sortino_ratio | -4.6066 |
| max_drawdown | 0.9968 |
| cagr | -0.8988 |
| net_avg_win | 13.6348 |
| net_avg_loss | -24.5920 |
| avg_hold_time_bars | 4.6285 |
| exposure | 0.2514 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
