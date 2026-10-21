# EMA Hourly Continuation — GRAM/USDT P26_100

**Symbol:** GRAM/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.6743 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9103 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -2.5977 |
| sortino_ratio | -0.7823 |
| max_drawdown | 0.6200 |
| cagr | -0.3009 |
| net_avg_win | 58.2009 |
| net_avg_loss | -77.8243 |
| avg_hold_time_bars | 15.5416 |
| exposure | 0.3144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
