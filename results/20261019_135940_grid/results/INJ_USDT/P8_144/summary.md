# EMA Hourly Continuation — INJ/USDT P8_144

**Symbol:** INJ/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.6347 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8670 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -3.2767 |
| sortino_ratio | -1.0003 |
| max_drawdown | 0.7063 |
| cagr | -0.3789 |
| net_avg_win | 56.1187 |
| net_avg_loss | -74.0204 |
| avg_hold_time_bars | 35.1899 |
| exposure | 0.7582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
