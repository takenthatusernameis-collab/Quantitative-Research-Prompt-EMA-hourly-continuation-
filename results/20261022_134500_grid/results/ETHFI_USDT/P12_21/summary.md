# EMA Hourly Continuation — ETHFI/USDT P12_21

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1534 |
| net_profit_factor | 0.4147 |
| net_win_rate | 0.4074 |
| gross_profit_factor | 0.8502 |
| gross_win_rate | 0.4257 |
| sharpe_ratio | -12.3323 |
| sortino_ratio | -6.8483 |
| max_drawdown | 0.9998 |
| cagr | -0.9682 |
| net_avg_win | 11.3326 |
| net_avg_loss | -18.7911 |
| avg_hold_time_bars | 2.2080 |
| exposure | 0.1540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
