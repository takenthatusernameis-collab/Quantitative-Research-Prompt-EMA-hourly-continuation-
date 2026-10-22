# EMA Hourly Continuation — SEI/USDT P34_50

**Symbol:** SEI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 889 |
| net_profit_factor | 0.4088 |
| net_win_rate | 0.4207 |
| gross_profit_factor | 0.8091 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -9.2444 |
| sortino_ratio | -3.8888 |
| max_drawdown | 0.9936 |
| cagr | -0.8650 |
| net_avg_win | 18.3711 |
| net_avg_loss | -32.6318 |
| avg_hold_time_bars | 2.7672 |
| exposure | 0.1118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
