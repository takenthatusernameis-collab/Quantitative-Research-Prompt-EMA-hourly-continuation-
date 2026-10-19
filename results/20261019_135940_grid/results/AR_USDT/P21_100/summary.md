# EMA Hourly Continuation — AR/USDT P21_100

**Symbol:** AR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.6331 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.9059 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -3.7163 |
| sortino_ratio | -1.3326 |
| max_drawdown | 0.8064 |
| cagr | -0.4724 |
| net_avg_win | 44.9185 |
| net_avg_loss | -62.9570 |
| avg_hold_time_bars | 13.6263 |
| exposure | 0.4045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
