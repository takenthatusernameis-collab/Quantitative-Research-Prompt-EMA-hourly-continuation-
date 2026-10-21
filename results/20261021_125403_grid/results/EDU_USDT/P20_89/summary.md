# EMA Hourly Continuation — EDU/USDT P20_89

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.7751 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9718 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -1.8109 |
| sortino_ratio | -0.6209 |
| max_drawdown | 0.5311 |
| cagr | -0.2500 |
| net_avg_win | 61.9737 |
| net_avg_loss | -79.1251 |
| avg_hold_time_bars | 14.6222 |
| exposure | 0.3818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
