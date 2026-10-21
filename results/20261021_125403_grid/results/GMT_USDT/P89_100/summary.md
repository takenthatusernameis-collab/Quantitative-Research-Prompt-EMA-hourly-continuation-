# EMA Hourly Continuation — GMT/USDT P89_100

**Symbol:** GMT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 108 |
| net_profit_factor | 0.6820 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9741 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -1.2692 |
| sortino_ratio | -0.1895 |
| max_drawdown | 0.2211 |
| cagr | -0.0829 |
| net_avg_win | 79.0374 |
| net_avg_loss | -111.6806 |
| avg_hold_time_bars | 4.6481 |
| exposure | 0.0228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
