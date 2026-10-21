# EMA Hourly Continuation — CTSI/USDT P89_200

**Symbol:** CTSI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7164 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9429 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -2.0449 |
| sortino_ratio | -0.5336 |
| max_drawdown | 0.4666 |
| cagr | -0.2174 |
| net_avg_win | 72.5850 |
| net_avg_loss | -93.1669 |
| avg_hold_time_bars | 14.5569 |
| exposure | 0.2210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
