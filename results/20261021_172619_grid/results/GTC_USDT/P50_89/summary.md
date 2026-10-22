# EMA Hourly Continuation — GTC/USDT P50_89

**Symbol:** GTC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6735 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9186 |
| gross_win_rate | 0.4774 |
| sharpe_ratio | -2.6046 |
| sortino_ratio | -0.7623 |
| max_drawdown | 0.6108 |
| cagr | -0.2959 |
| net_avg_win | 60.4085 |
| net_avg_loss | -81.1698 |
| avg_hold_time_bars | 7.5582 |
| exposure | 0.1446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
