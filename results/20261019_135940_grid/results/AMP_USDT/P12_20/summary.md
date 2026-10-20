# EMA Hourly Continuation — AMP/USDT P12_20

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1893 |
| net_profit_factor | 0.1464 |
| net_win_rate | 0.3006 |
| gross_profit_factor | 0.4777 |
| gross_win_rate | 0.3555 |
| sharpe_ratio | -20.6426 |
| sortino_ratio | -13.0598 |
| max_drawdown | 1.0000 |
| cagr | -0.9991 |
| net_avg_win | 3.0143 |
| net_avg_loss | -8.8483 |
| avg_hold_time_bars | 2.2198 |
| exposure | 0.1910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
