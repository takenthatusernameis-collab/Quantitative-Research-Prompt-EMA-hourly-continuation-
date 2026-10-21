# EMA Hourly Continuation — MOVR/USDT P12_21

**Symbol:** MOVR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.6286 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.8979 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -2.9460 |
| sortino_ratio | -0.8772 |
| max_drawdown | 0.6720 |
| cagr | -0.3299 |
| net_avg_win | 52.1020 |
| net_avg_loss | -75.5485 |
| avg_hold_time_bars | 4.6644 |
| exposure | 0.0916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
