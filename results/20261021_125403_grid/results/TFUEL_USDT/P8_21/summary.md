# EMA Hourly Continuation — TFUEL/USDT P8_21

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.5733 |
| net_win_rate | 0.4194 |
| gross_profit_factor | 0.8423 |
| gross_win_rate | 0.4194 |
| sharpe_ratio | -5.9303 |
| sortino_ratio | -2.1883 |
| max_drawdown | 0.9238 |
| cagr | -0.6369 |
| net_avg_win | 44.0974 |
| net_avg_loss | -55.5652 |
| avg_hold_time_bars | 5.5985 |
| exposure | 0.1697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
