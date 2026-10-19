# EMA Hourly Continuation — FET/USDT P89_100

**Symbol:** FET/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.3051 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.7052 |
| gross_win_rate | 0.4239 |
| sharpe_ratio | -8.1692 |
| sortino_ratio | -2.7228 |
| max_drawdown | 0.9734 |
| cagr | -0.7633 |
| net_avg_win | 19.6029 |
| net_avg_loss | -42.8296 |
| avg_hold_time_bars | 2.2385 |
| exposure | 0.0555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
