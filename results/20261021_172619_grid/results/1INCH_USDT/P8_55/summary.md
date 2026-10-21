# EMA Hourly Continuation — 1INCH/USDT P8_55

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.7285 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9586 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -2.7375 |
| sortino_ratio | -1.0209 |
| max_drawdown | 0.7061 |
| cagr | -0.3735 |
| net_avg_win | 55.6834 |
| net_avg_loss | -73.3509 |
| avg_hold_time_bars | 15.4162 |
| exposure | 0.4765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
