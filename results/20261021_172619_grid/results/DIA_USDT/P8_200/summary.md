# EMA Hourly Continuation — DIA/USDT P8_200

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 1.0236 |
| net_win_rate | 0.5495 |
| gross_profit_factor | 1.2082 |
| gross_win_rate | 0.5495 |
| sharpe_ratio | 0.1722 |
| sortino_ratio | 0.0427 |
| max_drawdown | 0.1931 |
| cagr | 0.0128 |
| net_avg_win | 88.0288 |
| net_avg_loss | -104.8937 |
| avg_hold_time_bars | 60.1126 |
| exposure | 0.7970 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
