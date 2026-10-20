# EMA Hourly Continuation — GMX/USDT P12_21

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1363 |
| net_profit_factor | 0.3190 |
| net_win_rate | 0.3984 |
| gross_profit_factor | 0.7704 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -12.6520 |
| sortino_ratio | -6.6845 |
| max_drawdown | 0.9998 |
| cagr | -0.9652 |
| net_avg_win | 8.6253 |
| net_avg_loss | -17.9041 |
| avg_hold_time_bars | 3.1577 |
| exposure | 0.1956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
