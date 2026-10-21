# EMA Hourly Continuation — BNB/USDT P21_200

**Symbol:** BNB/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.7657 |
| net_win_rate | 0.5382 |
| gross_profit_factor | 1.1543 |
| gross_win_rate | 0.5382 |
| sharpe_ratio | -1.4055 |
| sortino_ratio | -0.3673 |
| max_drawdown | 0.3856 |
| cagr | -0.1533 |
| net_avg_win | 63.4559 |
| net_avg_loss | -96.5887 |
| avg_hold_time_bars | 40.4251 |
| exposure | 0.6009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
