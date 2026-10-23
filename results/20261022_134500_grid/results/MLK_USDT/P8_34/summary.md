# EMA Hourly Continuation — MLK/USDT P8_34

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1664 |
| net_profit_factor | 0.2678 |
| net_win_rate | 0.2855 |
| gross_profit_factor | 0.5941 |
| gross_win_rate | 0.2987 |
| sharpe_ratio | -18.0750 |
| sortino_ratio | -10.5301 |
| max_drawdown | 1.0000 |
| cagr | -0.9958 |
| net_avg_win | 7.7018 |
| net_avg_loss | -11.4873 |
| avg_hold_time_bars | 4.5649 |
| exposure | 0.3438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
