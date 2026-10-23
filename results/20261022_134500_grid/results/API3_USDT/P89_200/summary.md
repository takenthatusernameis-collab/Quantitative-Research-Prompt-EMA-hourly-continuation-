# EMA Hourly Continuation — API3/USDT P89_200

**Symbol:** API3/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.7980 |
| net_win_rate | 0.5264 |
| gross_profit_factor | 1.1365 |
| gross_win_rate | 0.5340 |
| sharpe_ratio | -1.4175 |
| sortino_ratio | -0.4041 |
| max_drawdown | 0.3980 |
| cagr | -0.1728 |
| net_avg_win | 71.6402 |
| net_avg_loss | -99.7978 |
| avg_hold_time_bars | 10.6801 |
| exposure | 0.1927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
