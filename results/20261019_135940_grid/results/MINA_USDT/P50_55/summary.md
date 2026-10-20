# EMA Hourly Continuation — MINA/USDT P50_55

**Symbol:** MINA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 855 |
| net_profit_factor | 0.2704 |
| net_win_rate | 0.3754 |
| gross_profit_factor | 0.8199 |
| gross_win_rate | 0.4281 |
| sharpe_ratio | -11.9093 |
| sortino_ratio | -5.0771 |
| max_drawdown | 0.9990 |
| cagr | -0.9355 |
| net_avg_win | 11.5315 |
| net_avg_loss | -25.6392 |
| avg_hold_time_bars | 2.1567 |
| exposure | 0.0838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
