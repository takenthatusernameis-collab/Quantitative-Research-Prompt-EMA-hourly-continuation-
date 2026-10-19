# EMA Hourly Continuation — DOGE/USDT P34_200

**Symbol:** DOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.5557 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8524 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -3.5336 |
| sortino_ratio | -0.9142 |
| max_drawdown | 0.7070 |
| cagr | -0.3723 |
| net_avg_win | 52.2669 |
| net_avg_loss | -82.5450 |
| avg_hold_time_bars | 31.1615 |
| exposure | 0.5000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
