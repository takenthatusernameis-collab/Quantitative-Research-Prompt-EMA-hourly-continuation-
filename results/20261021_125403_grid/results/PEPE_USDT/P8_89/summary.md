# EMA Hourly Continuation — PEPE/USDT P8_89

**Symbol:** PEPE/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 1.0035 |
| net_win_rate | 0.5455 |
| gross_profit_factor | 1.1892 |
| gross_win_rate | 0.5455 |
| sharpe_ratio | 0.0912 |
| sortino_ratio | 0.0281 |
| max_drawdown | 0.1551 |
| cagr | 0.0033 |
| net_avg_win | 95.5119 |
| net_avg_loss | -114.2144 |
| avg_hold_time_bars | 30.3060 |
| exposure | 0.6213 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
