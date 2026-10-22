# EMA Hourly Continuation — BIGTIME/USDT P12_55

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.7841 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 0.9824 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -2.0249 |
| sortino_ratio | -0.7412 |
| max_drawdown | 0.6017 |
| cagr | -0.2897 |
| net_avg_win | 64.1891 |
| net_avg_loss | -81.1201 |
| avg_hold_time_bars | 11.6925 |
| exposure | 0.3476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
