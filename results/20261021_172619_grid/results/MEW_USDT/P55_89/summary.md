# EMA Hourly Continuation — MEW/USDT P55_89

**Symbol:** MEW/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.6382 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.8353 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -2.5362 |
| sortino_ratio | -0.6559 |
| max_drawdown | 0.5354 |
| cagr | -0.2597 |
| net_avg_win | 61.9340 |
| net_avg_loss | -81.8616 |
| avg_hold_time_bars | 7.0515 |
| exposure | 0.1058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
