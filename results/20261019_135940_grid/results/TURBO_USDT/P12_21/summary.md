# EMA Hourly Continuation — TURBO/USDT P12_21

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1268 |
| net_profit_factor | 0.4057 |
| net_win_rate | 0.4085 |
| gross_profit_factor | 0.7371 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -12.0612 |
| sortino_ratio | -6.6762 |
| max_drawdown | 0.9991 |
| cagr | -0.9650 |
| net_avg_win | 13.1659 |
| net_avg_loss | -22.4146 |
| avg_hold_time_bars | 2.1546 |
| exposure | 0.1490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
