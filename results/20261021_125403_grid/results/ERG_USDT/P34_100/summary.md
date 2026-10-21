# EMA Hourly Continuation — ERG/USDT P34_100

**Symbol:** ERG/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.5541 |
| net_win_rate | 0.4271 |
| gross_profit_factor | 0.7132 |
| gross_win_rate | 0.4271 |
| sharpe_ratio | -3.3517 |
| sortino_ratio | -0.9303 |
| max_drawdown | 0.6682 |
| cagr | -0.3487 |
| net_avg_win | 49.9506 |
| net_avg_loss | -67.2027 |
| avg_hold_time_bars | 13.4870 |
| exposure | 0.2354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
