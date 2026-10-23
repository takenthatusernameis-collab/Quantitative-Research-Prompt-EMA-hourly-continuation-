# EMA Hourly Continuation — TRADE/USDT P26_144

**Symbol:** TRADE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.6581 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8529 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -2.6230 |
| sortino_ratio | -0.7265 |
| max_drawdown | 0.6162 |
| cagr | -0.2947 |
| net_avg_win | 62.0890 |
| net_avg_loss | -81.3201 |
| avg_hold_time_bars | 25.4885 |
| exposure | 0.4530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
