# EMA Hourly Continuation — BTC/USDT P26_34

**Symbol:** BTC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1150 |
| net_profit_factor | 0.0726 |
| net_win_rate | 0.2574 |
| gross_profit_factor | 0.7088 |
| gross_win_rate | 0.4191 |
| sharpe_ratio | -17.9000 |
| sortino_ratio | -9.1951 |
| max_drawdown | 1.0000 |
| cagr | -0.9937 |
| net_avg_win | 2.6460 |
| net_avg_loss | -12.6267 |
| avg_hold_time_bars | 2.2548 |
| exposure | 0.1037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
