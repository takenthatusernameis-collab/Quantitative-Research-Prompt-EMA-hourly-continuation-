# EMA Hourly Continuation — XTZ/USDT P12_200

**Symbol:** XTZ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.6628 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9706 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -2.2390 |
| sortino_ratio | -0.5554 |
| max_drawdown | 0.4949 |
| cagr | -0.2299 |
| net_avg_win | 64.7695 |
| net_avg_loss | -89.1711 |
| avg_hold_time_bars | 57.1830 |
| exposure | 0.7954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
