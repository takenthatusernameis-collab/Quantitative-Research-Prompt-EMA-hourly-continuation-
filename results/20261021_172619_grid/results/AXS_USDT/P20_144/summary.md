# EMA Hourly Continuation — AXS/USDT P20_144

**Symbol:** AXS/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.9211 |
| net_win_rate | 0.5303 |
| gross_profit_factor | 1.1256 |
| gross_win_rate | 0.5303 |
| sharpe_ratio | -0.4363 |
| sortino_ratio | -0.1169 |
| max_drawdown | 0.2320 |
| cagr | -0.0564 |
| net_avg_win | 86.3933 |
| net_avg_loss | -105.8813 |
| avg_hold_time_bars | 35.4207 |
| exposure | 0.5562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
