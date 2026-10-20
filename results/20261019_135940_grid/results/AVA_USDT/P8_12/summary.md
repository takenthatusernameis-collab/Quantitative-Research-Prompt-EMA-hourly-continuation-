# EMA Hourly Continuation — AVA/USDT P8_12

**Symbol:** AVA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1701 |
| net_profit_factor | 0.2046 |
| net_win_rate | 0.3563 |
| gross_profit_factor | 0.7751 |
| gross_win_rate | 0.4156 |
| sharpe_ratio | -17.8445 |
| sortino_ratio | -10.7110 |
| max_drawdown | 1.0000 |
| cagr | -0.9970 |
| net_avg_win | 4.2444 |
| net_avg_loss | -11.4814 |
| avg_hold_time_bars | 1.8242 |
| exposure | 0.1410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
