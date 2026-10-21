# EMA Hourly Continuation — SNX/USDT P8_200

**Symbol:** SNX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 1.0100 |
| net_win_rate | 0.5440 |
| gross_profit_factor | 1.1879 |
| gross_win_rate | 0.5440 |
| sharpe_ratio | 0.1093 |
| sortino_ratio | 0.0277 |
| max_drawdown | 0.1156 |
| cagr | 0.0060 |
| net_avg_win | 91.8563 |
| net_avg_loss | -108.4880 |
| avg_hold_time_bars | 56.7264 |
| exposure | 0.7880 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
