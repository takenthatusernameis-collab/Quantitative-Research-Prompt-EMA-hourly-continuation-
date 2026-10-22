# EMA Hourly Continuation — ILV/USDT P12_200

**Symbol:** ILV/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 1.0059 |
| net_win_rate | 0.5462 |
| gross_profit_factor | 1.1824 |
| gross_win_rate | 0.5462 |
| sharpe_ratio | 0.0789 |
| sortino_ratio | 0.0176 |
| max_drawdown | 0.1565 |
| cagr | 0.0029 |
| net_avg_win | 97.2723 |
| net_avg_loss | -116.4006 |
| avg_hold_time_bars | 72.4076 |
| exposure | 0.7833 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
