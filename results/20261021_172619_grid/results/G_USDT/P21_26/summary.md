# EMA Hourly Continuation — G/USDT P21_26

**Symbol:** G/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.6801 |
| net_win_rate | 0.5168 |
| gross_profit_factor | 1.1259 |
| gross_win_rate | 0.5199 |
| sharpe_ratio | -2.5249 |
| sortino_ratio | -0.7101 |
| max_drawdown | 0.5318 |
| cagr | -0.2746 |
| net_avg_win | 63.1408 |
| net_avg_loss | -99.3001 |
| avg_hold_time_bars | 5.5872 |
| exposure | 0.0961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
