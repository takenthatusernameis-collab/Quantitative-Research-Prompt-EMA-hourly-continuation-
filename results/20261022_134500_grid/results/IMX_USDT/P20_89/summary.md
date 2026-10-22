# EMA Hourly Continuation — IMX/USDT P20_89

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.6761 |
| net_win_rate | 0.4955 |
| gross_profit_factor | 0.9903 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -2.9011 |
| sortino_ratio | -1.0517 |
| max_drawdown | 0.7214 |
| cagr | -0.3935 |
| net_avg_win | 45.6243 |
| net_avg_loss | -66.2652 |
| avg_hold_time_bars | 13.2719 |
| exposure | 0.3976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
