# EMA Hourly Continuation — DEEP/USDT P8_200

**Symbol:** DEEP/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 189 |
| net_profit_factor | 0.7579 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9154 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -1.3567 |
| sortino_ratio | -0.2923 |
| max_drawdown | 0.2783 |
| cagr | -0.1306 |
| net_avg_win | 84.5652 |
| net_avg_loss | -103.6090 |
| avg_hold_time_bars | 80.7778 |
| exposure | 0.8644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
