# EMA Hourly Continuation — XLM/USDT P20_100

**Symbol:** XLM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.8520 |
| net_win_rate | 0.5327 |
| gross_profit_factor | 1.1312 |
| gross_win_rate | 0.5327 |
| sharpe_ratio | -0.9531 |
| sortino_ratio | -0.2897 |
| max_drawdown | 0.3223 |
| cagr | -0.1268 |
| net_avg_win | 70.3842 |
| net_avg_loss | -94.1850 |
| avg_hold_time_bars | 21.4628 |
| exposure | 0.4322 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
