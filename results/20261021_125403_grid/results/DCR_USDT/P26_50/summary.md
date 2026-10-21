# EMA Hourly Continuation — DCR/USDT P26_50

**Symbol:** DCR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.5463 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8080 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -4.0759 |
| sortino_ratio | -1.2845 |
| max_drawdown | 0.7911 |
| cagr | -0.4482 |
| net_avg_win | 42.5186 |
| net_avg_loss | -63.4177 |
| avg_hold_time_bars | 6.0673 |
| exposure | 0.1345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
