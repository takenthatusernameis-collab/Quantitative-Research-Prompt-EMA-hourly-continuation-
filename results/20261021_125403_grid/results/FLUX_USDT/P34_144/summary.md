# EMA Hourly Continuation — FLUX/USDT P34_144

**Symbol:** FLUX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.7751 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9562 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -1.5014 |
| sortino_ratio | -0.4189 |
| max_drawdown | 0.4270 |
| cagr | -0.1758 |
| net_avg_win | 70.8933 |
| net_avg_loss | -88.1656 |
| avg_hold_time_bars | 21.7822 |
| exposure | 0.3772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
