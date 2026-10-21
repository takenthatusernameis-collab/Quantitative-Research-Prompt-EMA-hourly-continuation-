# EMA Hourly Continuation — ATH/USDT P12_144

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 1.0087 |
| net_win_rate | 0.5449 |
| gross_profit_factor | 1.1787 |
| gross_win_rate | 0.5449 |
| sharpe_ratio | 0.1107 |
| sortino_ratio | 0.0297 |
| max_drawdown | 0.1214 |
| cagr | 0.0061 |
| net_avg_win | 95.3637 |
| net_avg_loss | -113.1919 |
| avg_hold_time_bars | 44.2601 |
| exposure | 0.6929 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
