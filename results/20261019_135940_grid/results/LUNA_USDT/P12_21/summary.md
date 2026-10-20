# EMA Hourly Continuation — LUNA/USDT P12_21

**Symbol:** LUNA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1599 |
| net_profit_factor | 0.2176 |
| net_win_rate | 0.3609 |
| gross_profit_factor | 0.6531 |
| gross_win_rate | 0.3971 |
| sharpe_ratio | -16.5260 |
| sortino_ratio | -9.4969 |
| max_drawdown | 1.0000 |
| cagr | -0.9938 |
| net_avg_win | 4.8188 |
| net_avg_loss | -12.5053 |
| avg_hold_time_bars | 2.0976 |
| exposure | 0.1525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
