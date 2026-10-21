# EMA Hourly Continuation — BTC/USDT P21_26

**Symbol:** BTC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 164 |
| net_profit_factor | 0.5152 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.1000 |
| gross_win_rate | 0.5305 |
| sharpe_ratio | -2.2625 |
| sortino_ratio | -0.3934 |
| max_drawdown | 0.4056 |
| cagr | -0.1658 |
| net_avg_win | 49.8930 |
| net_avg_loss | -106.7820 |
| avg_hold_time_bars | 5.8110 |
| exposure | 0.0381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
