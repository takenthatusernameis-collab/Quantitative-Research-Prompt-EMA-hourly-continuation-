# EMA Hourly Continuation — XAI/USDT P50_100

**Symbol:** XAI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.6954 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.8890 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -2.2800 |
| sortino_ratio | -0.6481 |
| max_drawdown | 0.5775 |
| cagr | -0.2573 |
| net_avg_win | 63.9207 |
| net_avg_loss | -82.6792 |
| avg_hold_time_bars | 10.5063 |
| exposure | 0.1896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
