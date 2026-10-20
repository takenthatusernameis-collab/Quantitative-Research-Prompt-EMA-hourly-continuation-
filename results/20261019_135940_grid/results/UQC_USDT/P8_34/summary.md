# EMA Hourly Continuation — UQC/USDT P8_34

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 553 |
| net_profit_factor | 0.2046 |
| net_win_rate | 0.2948 |
| gross_profit_factor | 0.5396 |
| gross_win_rate | 0.3183 |
| sharpe_ratio | -9.9217 |
| sortino_ratio | -3.3003 |
| max_drawdown | 0.9896 |
| cagr | -0.8355 |
| net_avg_win | 15.6107 |
| net_avg_loss | -31.8952 |
| avg_hold_time_bars | 24.3201 |
| exposure | 0.6087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
