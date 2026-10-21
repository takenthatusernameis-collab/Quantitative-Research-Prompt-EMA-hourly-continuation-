# EMA Hourly Continuation — ONDO/USDT P55_144

**Symbol:** ONDO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.6857 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8426 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -2.0572 |
| sortino_ratio | -0.5160 |
| max_drawdown | 0.4617 |
| cagr | -0.2109 |
| net_avg_win | 68.3955 |
| net_avg_loss | -84.4015 |
| avg_hold_time_bars | 15.3494 |
| exposure | 0.2177 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
