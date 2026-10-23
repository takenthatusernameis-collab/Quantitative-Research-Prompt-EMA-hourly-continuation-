# EMA Hourly Continuation — MEW/USDT P20_55

**Symbol:** MEW/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.4977 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.7735 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -6.0802 |
| sortino_ratio | -2.5993 |
| max_drawdown | 0.9594 |
| cagr | -0.7183 |
| net_avg_win | 22.1859 |
| net_avg_loss | -37.8578 |
| avg_hold_time_bars | 5.4174 |
| exposure | 0.2295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
