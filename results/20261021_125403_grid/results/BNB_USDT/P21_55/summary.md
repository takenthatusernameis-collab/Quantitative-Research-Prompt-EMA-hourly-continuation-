# EMA Hourly Continuation — BNB/USDT P21_55

**Symbol:** BNB/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.6118 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0684 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -3.4492 |
| sortino_ratio | -1.0797 |
| max_drawdown | 0.7199 |
| cagr | -0.3896 |
| net_avg_win | 46.6573 |
| net_avg_loss | -79.9260 |
| avg_hold_time_bars | 7.9446 |
| exposure | 0.1694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
