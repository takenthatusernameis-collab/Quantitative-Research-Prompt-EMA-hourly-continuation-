# EMA Hourly Continuation — MANTA/USDT P8_12

**Symbol:** MANTA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1865 |
| net_profit_factor | 0.2324 |
| net_win_rate | 0.3796 |
| gross_profit_factor | 0.7030 |
| gross_win_rate | 0.4247 |
| sharpe_ratio | -16.6289 |
| sortino_ratio | -10.2819 |
| max_drawdown | 1.0000 |
| cagr | -0.9954 |
| net_avg_win | 4.2764 |
| net_avg_loss | -11.2599 |
| avg_hold_time_bars | 2.0295 |
| exposure | 0.1720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
