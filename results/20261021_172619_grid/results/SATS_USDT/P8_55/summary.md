# EMA Hourly Continuation — SATS/USDT P8_55

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.8033 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 0.9745 |
| gross_win_rate | 0.4911 |
| sharpe_ratio | -1.9313 |
| sortino_ratio | -0.7138 |
| max_drawdown | 0.5755 |
| cagr | -0.2814 |
| net_avg_win | 69.9711 |
| net_avg_loss | -84.0506 |
| avg_hold_time_bars | 15.5565 |
| exposure | 0.4731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
