# EMA Hourly Continuation — LPT/USDT P20_200

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6432 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8613 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -2.8206 |
| sortino_ratio | -0.8288 |
| max_drawdown | 0.6732 |
| cagr | -0.3215 |
| net_avg_win | 55.2783 |
| net_avg_loss | -75.2013 |
| avg_hold_time_bars | 30.4184 |
| exposure | 0.6015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
