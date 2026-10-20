# EMA Hourly Continuation — CFG/USDT P12_100

**Symbol:** CFG/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.5834 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8517 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -3.8508 |
| sortino_ratio | -1.3441 |
| max_drawdown | 0.8071 |
| cagr | -0.4724 |
| net_avg_win | 40.1161 |
| net_avg_loss | -56.7591 |
| avg_hold_time_bars | 22.7326 |
| exposure | 0.6375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
