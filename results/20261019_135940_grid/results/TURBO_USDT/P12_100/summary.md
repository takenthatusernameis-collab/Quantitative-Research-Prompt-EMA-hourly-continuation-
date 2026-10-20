# EMA Hourly Continuation — TURBO/USDT P12_100

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 602 |
| net_profit_factor | 0.6914 |
| net_win_rate | 0.4718 |
| gross_profit_factor | 0.9484 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -3.7137 |
| sortino_ratio | -1.4065 |
| max_drawdown | 0.7714 |
| cagr | -0.4881 |
| net_avg_win | 59.4586 |
| net_avg_loss | -76.8028 |
| avg_hold_time_bars | 16.5033 |
| exposure | 0.5420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
