# EMA Hourly Continuation — BOME/USDT P21_144

**Symbol:** BOME/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.8668 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0083 |
| gross_win_rate | 0.5072 |
| sharpe_ratio | -0.7386 |
| sortino_ratio | -0.1971 |
| max_drawdown | 0.2592 |
| cagr | -0.0896 |
| net_avg_win | 77.6288 |
| net_avg_loss | -92.1737 |
| avg_hold_time_bars | 34.5677 |
| exposure | 0.5452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
