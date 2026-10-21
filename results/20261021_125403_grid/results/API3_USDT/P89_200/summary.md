# EMA Hourly Continuation — API3/USDT P89_200

**Symbol:** API3/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.8588 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0796 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -0.7949 |
| sortino_ratio | -0.2014 |
| max_drawdown | 0.2858 |
| cagr | -0.0908 |
| net_avg_win | 79.8764 |
| net_avg_loss | -101.8027 |
| avg_hold_time_bars | 13.1032 |
| exposure | 0.1846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
