# EMA Hourly Continuation — SKY/USDT P8_26

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.6713 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 0.9932 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -3.4951 |
| sortino_ratio | -1.4032 |
| max_drawdown | 0.7374 |
| cagr | -0.4718 |
| net_avg_win | 46.9951 |
| net_avg_loss | -69.3456 |
| avg_hold_time_bars | 6.0016 |
| exposure | 0.2132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
