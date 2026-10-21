# EMA Hourly Continuation — AUCTION/USDT P12_34

**Symbol:** AUCTION/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.5540 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 0.7843 |
| gross_win_rate | 0.4305 |
| sharpe_ratio | -5.4593 |
| sortino_ratio | -2.0026 |
| max_drawdown | 0.9094 |
| cagr | -0.6085 |
| net_avg_win | 39.0870 |
| net_avg_loss | -53.3279 |
| avg_hold_time_bars | 8.3931 |
| exposure | 0.2541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
