# EMA Hourly Continuation — IMX/USDT P12_20

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1469 |
| net_profit_factor | 0.3399 |
| net_win_rate | 0.4050 |
| gross_profit_factor | 0.7588 |
| gross_win_rate | 0.4329 |
| sharpe_ratio | -12.8314 |
| sortino_ratio | -6.9540 |
| max_drawdown | 0.9999 |
| cagr | -0.9727 |
| net_avg_win | 8.6521 |
| net_avg_loss | -17.3305 |
| avg_hold_time_bars | 2.2321 |
| exposure | 0.1484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
