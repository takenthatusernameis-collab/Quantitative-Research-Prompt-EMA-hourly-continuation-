# EMA Hourly Continuation — SUPER/USDT P34_144

**Symbol:** SUPER/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.8710 |
| net_win_rate | 0.5228 |
| gross_profit_factor | 1.0668 |
| gross_win_rate | 0.5228 |
| sharpe_ratio | -0.7090 |
| sortino_ratio | -0.1970 |
| max_drawdown | 0.3090 |
| cagr | -0.0895 |
| net_avg_win | 72.6679 |
| net_avg_loss | -91.3976 |
| avg_hold_time_bars | 22.4718 |
| exposure | 0.3810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
