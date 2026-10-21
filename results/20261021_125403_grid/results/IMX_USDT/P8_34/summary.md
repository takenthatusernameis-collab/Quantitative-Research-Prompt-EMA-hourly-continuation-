# EMA Hourly Continuation — IMX/USDT P8_34

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 735 |
| net_profit_factor | 0.7955 |
| net_win_rate | 0.5007 |
| gross_profit_factor | 1.0106 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -2.0738 |
| sortino_ratio | -0.8041 |
| max_drawdown | 0.6344 |
| cagr | -0.3103 |
| net_avg_win | 64.2876 |
| net_avg_loss | -81.0361 |
| avg_hold_time_bars | 9.0313 |
| exposure | 0.3004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
