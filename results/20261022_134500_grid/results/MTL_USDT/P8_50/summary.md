# EMA Hourly Continuation — MTL/USDT P8_50

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 916 |
| net_profit_factor | 0.6192 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 1.0058 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -5.6110 |
| sortino_ratio | -2.3908 |
| max_drawdown | 0.9486 |
| cagr | -0.6840 |
| net_avg_win | 35.9951 |
| net_avg_loss | -50.7627 |
| avg_hold_time_bars | 13.0175 |
| exposure | 0.5396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
