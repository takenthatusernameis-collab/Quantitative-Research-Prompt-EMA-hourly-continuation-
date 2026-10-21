# EMA Hourly Continuation — DCR/USDT P12_34

**Symbol:** DCR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.6987 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 1.0032 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -3.1044 |
| sortino_ratio | -1.1640 |
| max_drawdown | 0.7615 |
| cagr | -0.4134 |
| net_avg_win | 50.5808 |
| net_avg_loss | -70.5251 |
| avg_hold_time_bars | 6.8908 |
| exposure | 0.2142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
