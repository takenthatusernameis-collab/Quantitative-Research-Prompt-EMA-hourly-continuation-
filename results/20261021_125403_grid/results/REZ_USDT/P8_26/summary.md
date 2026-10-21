# EMA Hourly Continuation — REZ/USDT P8_26

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 755 |
| net_profit_factor | 0.8006 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0201 |
| gross_win_rate | 0.5020 |
| sharpe_ratio | -2.1894 |
| sortino_ratio | -0.8688 |
| max_drawdown | 0.6703 |
| cagr | -0.3304 |
| net_avg_win | 66.6597 |
| net_avg_loss | -83.9297 |
| avg_hold_time_bars | 6.4583 |
| exposure | 0.2250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
