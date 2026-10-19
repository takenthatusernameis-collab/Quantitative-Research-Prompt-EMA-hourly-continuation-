# EMA Hourly Continuation — XDC/USDT P26_200

**Symbol:** XDC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.5231 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8774 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -4.3785 |
| sortino_ratio | -1.3584 |
| max_drawdown | 0.8161 |
| cagr | -0.4878 |
| net_avg_win | 39.6669 |
| net_avg_loss | -64.1407 |
| avg_hold_time_bars | 23.3279 |
| exposure | 0.5206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
