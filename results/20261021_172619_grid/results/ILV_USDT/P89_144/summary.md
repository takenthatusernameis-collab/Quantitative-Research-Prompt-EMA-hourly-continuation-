# EMA Hourly Continuation — ILV/USDT P89_144

**Symbol:** ILV/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.8317 |
| net_win_rate | 0.5300 |
| gross_profit_factor | 1.1202 |
| gross_win_rate | 0.5300 |
| sharpe_ratio | -0.9753 |
| sortino_ratio | -0.2439 |
| max_drawdown | 0.2519 |
| cagr | -0.1070 |
| net_avg_win | 76.8611 |
| net_avg_loss | -104.2154 |
| avg_hold_time_bars | 7.5833 |
| exposure | 0.1034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
