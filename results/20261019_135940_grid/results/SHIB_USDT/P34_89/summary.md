# EMA Hourly Continuation — SHIB/USDT P34_89

**Symbol:** SHIB/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.5020 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.8841 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -6.2105 |
| sortino_ratio | -2.3581 |
| max_drawdown | 0.9497 |
| cagr | -0.6855 |
| net_avg_win | 28.7899 |
| net_avg_loss | -48.0556 |
| avg_hold_time_bars | 6.7452 |
| exposure | 0.2226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
