# EMA Hourly Continuation — REZ/USDT P12_20

**Symbol:** REZ/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.6795 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.9201 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -2.7503 |
| sortino_ratio | -0.8111 |
| max_drawdown | 0.6313 |
| cagr | -0.3113 |
| net_avg_win | 64.1947 |
| net_avg_loss | -85.0697 |
| avg_hold_time_bars | 4.9881 |
| exposure | 0.0967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
