# EMA Hourly Continuation — MANTA/USDT P12_100

**Symbol:** MANTA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.8321 |
| net_win_rate | 0.4967 |
| gross_profit_factor | 1.0115 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -1.4281 |
| sortino_ratio | -0.4376 |
| max_drawdown | 0.4587 |
| cagr | -0.1840 |
| net_avg_win | 86.9476 |
| net_avg_loss | -103.1326 |
| avg_hold_time_bars | 29.2200 |
| exposure | 0.6096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
