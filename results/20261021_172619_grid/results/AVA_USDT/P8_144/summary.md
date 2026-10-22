# EMA Hourly Continuation — AVA/USDT P8_144

**Symbol:** AVA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.8392 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0031 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -0.9658 |
| sortino_ratio | -0.2672 |
| max_drawdown | 0.4020 |
| cagr | -0.1176 |
| net_avg_win | 74.8217 |
| net_avg_loss | -90.6084 |
| avg_hold_time_bars | 42.5791 |
| exposure | 0.7219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
