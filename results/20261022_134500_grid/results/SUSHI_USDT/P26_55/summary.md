# EMA Hourly Continuation — SUSHI/USDT P26_55

**Symbol:** SUSHI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 945 |
| net_profit_factor | 0.4898 |
| net_win_rate | 0.4275 |
| gross_profit_factor | 0.8427 |
| gross_win_rate | 0.4423 |
| sharpe_ratio | -7.8002 |
| sortino_ratio | -3.3635 |
| max_drawdown | 0.9851 |
| cagr | -0.8100 |
| net_avg_win | 23.4060 |
| net_avg_loss | -35.6828 |
| avg_hold_time_bars | 4.3101 |
| exposure | 0.1843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
