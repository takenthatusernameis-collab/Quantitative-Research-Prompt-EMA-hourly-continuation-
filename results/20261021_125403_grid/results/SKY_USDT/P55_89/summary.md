# EMA Hourly Continuation — SKY/USDT P55_89

**Symbol:** SKY/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.8871 |
| net_win_rate | 0.5690 |
| gross_profit_factor | 1.2988 |
| gross_win_rate | 0.5690 |
| sharpe_ratio | -0.6294 |
| sortino_ratio | -0.1728 |
| max_drawdown | 0.2156 |
| cagr | -0.0787 |
| net_avg_win | 73.5479 |
| net_avg_loss | -109.4344 |
| avg_hold_time_bars | 6.6828 |
| exposure | 0.1081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
