# EMA Hourly Continuation — MLK/USDT P144_200

**Symbol:** MLK/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.2458 |
| net_win_rate | 0.2638 |
| gross_profit_factor | 0.4884 |
| gross_win_rate | 0.2749 |
| sharpe_ratio | -10.6137 |
| sortino_ratio | -3.5928 |
| max_drawdown | 0.9901 |
| cagr | -0.8391 |
| net_avg_win | 22.5643 |
| net_avg_loss | -32.8996 |
| avg_hold_time_bars | 4.8542 |
| exposure | 0.1191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
