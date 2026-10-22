# EMA Hourly Continuation — XTZ/USDT P26_200

**Symbol:** XTZ/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6638 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 1.0055 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -2.7780 |
| sortino_ratio | -0.7892 |
| max_drawdown | 0.6261 |
| cagr | -0.3147 |
| net_avg_win | 61.4210 |
| net_avg_loss | -85.9840 |
| avg_hold_time_bars | 31.0978 |
| exposure | 0.5781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
