# EMA Hourly Continuation — BCH/USDT P8_144

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.6335 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 1.0231 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -3.0524 |
| sortino_ratio | -0.8455 |
| max_drawdown | 0.6823 |
| cagr | -0.3458 |
| net_avg_win | 57.8207 |
| net_avg_loss | -86.4171 |
| avg_hold_time_bars | 43.0620 |
| exposure | 0.7888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
