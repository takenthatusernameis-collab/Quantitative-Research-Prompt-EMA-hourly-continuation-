# EMA Hourly Continuation — XMR/USDT P20_200

**Symbol:** XMR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.7807 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9784 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -1.7015 |
| sortino_ratio | -0.4875 |
| max_drawdown | 0.5116 |
| cagr | -0.2009 |
| net_avg_win | 77.8214 |
| net_avg_loss | -95.3230 |
| avg_hold_time_bars | 30.2208 |
| exposure | 0.5536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
