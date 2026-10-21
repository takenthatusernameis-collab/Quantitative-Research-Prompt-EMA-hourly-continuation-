# EMA Hourly Continuation — XMR/USDT P55_89

**Symbol:** XMR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.4708 |
| net_win_rate | 0.4054 |
| gross_profit_factor | 0.6662 |
| gross_win_rate | 0.4054 |
| sharpe_ratio | -3.2761 |
| sortino_ratio | -0.6938 |
| max_drawdown | 0.5609 |
| cagr | -0.2728 |
| net_avg_win | 54.4430 |
| net_avg_loss | -78.8390 |
| avg_hold_time_bars | 7.0721 |
| exposure | 0.0714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
