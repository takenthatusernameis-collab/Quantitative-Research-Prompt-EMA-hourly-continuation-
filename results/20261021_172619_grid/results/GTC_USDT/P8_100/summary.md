# EMA Hourly Continuation — GTC/USDT P8_100

**Symbol:** GTC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.7283 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8843 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -2.3065 |
| sortino_ratio | -0.7527 |
| max_drawdown | 0.6030 |
| cagr | -0.2929 |
| net_avg_win | 63.0603 |
| net_avg_loss | -76.3857 |
| avg_hold_time_bars | 25.8786 |
| exposure | 0.6199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
