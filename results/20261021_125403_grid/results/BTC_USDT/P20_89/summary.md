# EMA Hourly Continuation — BTC/USDT P20_89

**Symbol:** BTC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.7140 |
| net_win_rate | 0.5244 |
| gross_profit_factor | 1.1368 |
| gross_win_rate | 0.5305 |
| sharpe_ratio | -2.2676 |
| sortino_ratio | -0.6803 |
| max_drawdown | 0.5924 |
| cagr | -0.2667 |
| net_avg_win | 56.8257 |
| net_avg_loss | -87.7543 |
| avg_hold_time_bars | 19.7012 |
| exposure | 0.3877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
