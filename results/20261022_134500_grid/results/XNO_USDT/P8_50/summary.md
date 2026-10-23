# EMA Hourly Continuation — XNO/USDT P8_50

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1354 |
| net_profit_factor | 0.4740 |
| net_win_rate | 0.3907 |
| gross_profit_factor | 0.7797 |
| gross_win_rate | 0.4025 |
| sharpe_ratio | -10.4655 |
| sortino_ratio | -5.4044 |
| max_drawdown | 0.9988 |
| cagr | -0.9311 |
| net_avg_win | 17.0149 |
| net_avg_loss | -23.0167 |
| avg_hold_time_bars | 6.6721 |
| exposure | 0.4106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
