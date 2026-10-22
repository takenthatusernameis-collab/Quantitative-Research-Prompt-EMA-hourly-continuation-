# EMA Hourly Continuation — LTC/USDT P89_200

**Symbol:** LTC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.3430 |
| net_win_rate | 0.4197 |
| gross_profit_factor | 0.7512 |
| gross_win_rate | 0.4497 |
| sharpe_ratio | -5.9920 |
| sortino_ratio | -1.8130 |
| max_drawdown | 0.9023 |
| cagr | -0.5997 |
| net_avg_win | 23.9632 |
| net_avg_loss | -50.5302 |
| avg_hold_time_bars | 8.5589 |
| exposure | 0.1817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
