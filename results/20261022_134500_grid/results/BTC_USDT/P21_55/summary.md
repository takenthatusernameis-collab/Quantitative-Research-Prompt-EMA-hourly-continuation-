# EMA Hourly Continuation — BTC/USDT P21_55

**Symbol:** BTC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.2955 |
| net_win_rate | 0.4030 |
| gross_profit_factor | 1.0406 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -10.7336 |
| sortino_ratio | -4.5670 |
| max_drawdown | 0.9989 |
| cagr | -0.9086 |
| net_avg_win | 10.5004 |
| net_avg_loss | -23.9912 |
| avg_hold_time_bars | 5.7414 |
| exposure | 0.2274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
