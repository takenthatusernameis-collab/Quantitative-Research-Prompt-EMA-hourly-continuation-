# EMA Hourly Continuation — IOTX/USDT P34_89

**Symbol:** IOTX/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.7280 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9560 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -2.2669 |
| sortino_ratio | -0.6751 |
| max_drawdown | 0.5845 |
| cagr | -0.2659 |
| net_avg_win | 68.8059 |
| net_avg_loss | -88.6051 |
| avg_hold_time_bars | 11.2765 |
| exposure | 0.2225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
