# EMA Hourly Continuation — CRO/USDT P8_20

**Symbol:** CRO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1721 |
| net_profit_factor | 0.2514 |
| net_win_rate | 0.3777 |
| gross_profit_factor | 0.7842 |
| gross_win_rate | 0.4265 |
| sharpe_ratio | -16.2253 |
| sortino_ratio | -9.6512 |
| max_drawdown | 1.0000 |
| cagr | -0.9941 |
| net_avg_win | 5.1678 |
| net_avg_loss | -12.4734 |
| avg_hold_time_bars | 2.8844 |
| exposure | 0.2256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
