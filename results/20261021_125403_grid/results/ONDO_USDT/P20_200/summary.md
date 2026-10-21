# EMA Hourly Continuation — ONDO/USDT P20_200

**Symbol:** ONDO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.9479 |
| net_win_rate | 0.5265 |
| gross_profit_factor | 1.1081 |
| gross_win_rate | 0.5265 |
| sharpe_ratio | -0.2609 |
| sortino_ratio | -0.0674 |
| max_drawdown | 0.2755 |
| cagr | -0.0352 |
| net_avg_win | 92.7255 |
| net_avg_loss | -108.7585 |
| avg_hold_time_bars | 38.2866 |
| exposure | 0.5586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
