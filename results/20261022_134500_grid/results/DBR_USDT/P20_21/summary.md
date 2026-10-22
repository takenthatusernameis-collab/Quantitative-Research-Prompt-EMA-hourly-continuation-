# EMA Hourly Continuation — DBR/USDT P20_21

**Symbol:** DBR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 773 |
| net_profit_factor | 0.2009 |
| net_win_rate | 0.3195 |
| gross_profit_factor | 0.9071 |
| gross_win_rate | 0.4321 |
| sharpe_ratio | -15.0860 |
| sortino_ratio | -7.0680 |
| max_drawdown | 0.9997 |
| cagr | -0.9811 |
| net_avg_win | 10.1749 |
| net_avg_loss | -23.7827 |
| avg_hold_time_bars | 2.9754 |
| exposure | 0.1308 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
