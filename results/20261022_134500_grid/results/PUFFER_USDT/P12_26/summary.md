# EMA Hourly Continuation — PUFFER/USDT P12_26

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1015 |
| net_profit_factor | 0.4771 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.7997 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -8.3941 |
| sortino_ratio | -4.1963 |
| max_drawdown | 0.9849 |
| cagr | -0.8736 |
| net_avg_win | 20.0529 |
| net_avg_loss | -33.2090 |
| avg_hold_time_bars | 3.6197 |
| exposure | 0.2079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
