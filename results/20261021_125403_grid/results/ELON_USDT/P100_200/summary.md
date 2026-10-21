# EMA Hourly Continuation — ELON/USDT P100_200

**Symbol:** ELON/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.6640 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8646 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -2.0474 |
| sortino_ratio | -0.4966 |
| max_drawdown | 0.4703 |
| cagr | -0.2036 |
| net_avg_win | 63.2813 |
| net_avg_loss | -84.7156 |
| avg_hold_time_bars | 11.2595 |
| exposure | 0.1479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
