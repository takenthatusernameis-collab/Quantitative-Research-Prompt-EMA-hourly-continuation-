# EMA Hourly Continuation — IMX/USDT P8_34

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1318 |
| net_profit_factor | 0.5510 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.9070 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -6.9896 |
| sortino_ratio | -3.5508 |
| max_drawdown | 0.9887 |
| cagr | -0.8227 |
| net_avg_win | 19.8909 |
| net_avg_loss | -31.0103 |
| avg_hold_time_bars | 5.7747 |
| exposure | 0.3444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
