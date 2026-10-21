# EMA Hourly Continuation — MANTA/USDT P34_55

**Symbol:** MANTA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.6981 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9557 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.3289 |
| sortino_ratio | -0.6217 |
| max_drawdown | 0.5528 |
| cagr | -0.2483 |
| net_avg_win | 70.4225 |
| net_avg_loss | -94.1520 |
| avg_hold_time_bars | 5.4339 |
| exposure | 0.0860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
