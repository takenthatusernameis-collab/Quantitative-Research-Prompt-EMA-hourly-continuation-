# EMA Hourly Continuation — AVA/USDT P12_20

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1386 |
| net_profit_factor | 0.2192 |
| net_win_rate | 0.3810 |
| gross_profit_factor | 0.6615 |
| gross_win_rate | 0.4120 |
| sharpe_ratio | -14.3030 |
| sortino_ratio | -7.6621 |
| max_drawdown | 1.0000 |
| cagr | -0.9819 |
| net_avg_win | 5.3173 |
| net_avg_loss | -14.9267 |
| avg_hold_time_bars | 2.2958 |
| exposure | 0.1446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
