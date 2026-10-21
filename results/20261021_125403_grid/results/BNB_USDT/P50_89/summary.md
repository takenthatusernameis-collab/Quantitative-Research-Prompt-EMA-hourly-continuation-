# EMA Hourly Continuation — BNB/USDT P50_89

**Symbol:** BNB/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.5462 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0365 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -3.2615 |
| sortino_ratio | -0.8259 |
| max_drawdown | 0.6188 |
| cagr | -0.3134 |
| net_avg_win | 47.7701 |
| net_avg_loss | -89.1893 |
| avg_hold_time_bars | 7.4426 |
| exposure | 0.1032 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
