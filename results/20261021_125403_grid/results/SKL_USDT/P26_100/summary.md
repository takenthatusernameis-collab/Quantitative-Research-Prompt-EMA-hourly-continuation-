# EMA Hourly Continuation — SKL/USDT P26_100

**Symbol:** SKL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.7324 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.9048 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -2.2229 |
| sortino_ratio | -0.6638 |
| max_drawdown | 0.5799 |
| cagr | -0.2632 |
| net_avg_win | 70.8206 |
| net_avg_loss | -85.9091 |
| avg_hold_time_bars | 18.9136 |
| exposure | 0.3783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
