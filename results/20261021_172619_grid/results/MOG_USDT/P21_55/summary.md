# EMA Hourly Continuation — MOG/USDT P21_55

**Symbol:** MOG/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.8123 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9853 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -1.6636 |
| sortino_ratio | -0.5324 |
| max_drawdown | 0.5245 |
| cagr | -0.2182 |
| net_avg_win | 82.6504 |
| net_avg_loss | -99.1206 |
| avg_hold_time_bars | 8.7664 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
