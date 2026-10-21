# EMA Hourly Continuation — AVA/USDT P21_26

**Symbol:** AVA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 208 |
| net_profit_factor | 0.5738 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.8921 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -2.4184 |
| sortino_ratio | -0.5013 |
| max_drawdown | 0.4734 |
| cagr | -0.2052 |
| net_avg_win | 59.5888 |
| net_avg_loss | -94.3278 |
| avg_hold_time_bars | 4.3077 |
| exposure | 0.0407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
