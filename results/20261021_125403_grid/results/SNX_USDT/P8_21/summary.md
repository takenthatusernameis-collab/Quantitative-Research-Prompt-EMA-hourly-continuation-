# EMA Hourly Continuation — SNX/USDT P8_21

**Symbol:** SNX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.7730 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0726 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -2.0816 |
| sortino_ratio | -0.7527 |
| max_drawdown | 0.6147 |
| cagr | -0.2904 |
| net_avg_win | 60.3041 |
| net_avg_loss | -83.6431 |
| avg_hold_time_bars | 5.4272 |
| exposure | 0.1552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
