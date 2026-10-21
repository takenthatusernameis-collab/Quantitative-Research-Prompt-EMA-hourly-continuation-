# EMA Hourly Continuation — JASMY/USDT P89_100

**Symbol:** JASMY/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 76 |
| net_profit_factor | 1.2123 |
| net_win_rate | 0.6316 |
| gross_profit_factor | 1.6904 |
| gross_win_rate | 0.6316 |
| sharpe_ratio | 0.5523 |
| sortino_ratio | 0.0721 |
| max_drawdown | 0.0653 |
| cagr | 0.0288 |
| net_avg_win | 88.0627 |
| net_avg_loss | -124.5316 |
| avg_hold_time_bars | 7.1579 |
| exposure | 0.0247 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
