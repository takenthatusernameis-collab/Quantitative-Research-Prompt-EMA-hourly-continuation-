# EMA Hourly Continuation — LTC/USDT P26_50

**Symbol:** LTC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 985 |
| net_profit_factor | 0.2659 |
| net_win_rate | 0.4173 |
| gross_profit_factor | 0.7644 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -10.6120 |
| sortino_ratio | -4.7562 |
| max_drawdown | 0.9980 |
| cagr | -0.9151 |
| net_avg_win | 8.7963 |
| net_avg_loss | -23.6844 |
| avg_hold_time_bars | 3.0538 |
| exposure | 0.1367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
