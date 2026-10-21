# EMA Hourly Continuation — DEEP/USDT P12_20

**Symbol:** DEEP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 223 |
| net_profit_factor | 1.0111 |
| net_win_rate | 0.5785 |
| gross_profit_factor | 1.3566 |
| gross_win_rate | 0.5785 |
| sharpe_ratio | 0.1153 |
| sortino_ratio | 0.0281 |
| max_drawdown | 0.1817 |
| cagr | 0.0066 |
| net_avg_win | 94.8667 |
| net_avg_loss | -128.7647 |
| avg_hold_time_bars | 4.8251 |
| exposure | 0.0609 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
