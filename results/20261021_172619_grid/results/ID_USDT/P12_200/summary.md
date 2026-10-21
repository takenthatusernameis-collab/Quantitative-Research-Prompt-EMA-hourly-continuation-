# EMA Hourly Continuation — ID/USDT P12_200

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.9128 |
| net_win_rate | 0.5255 |
| gross_profit_factor | 1.0951 |
| gross_win_rate | 0.5255 |
| sharpe_ratio | -0.4630 |
| sortino_ratio | -0.1178 |
| max_drawdown | 0.1785 |
| cagr | -0.0561 |
| net_avg_win | 85.9503 |
| net_avg_loss | -104.2690 |
| avg_hold_time_bars | 51.0732 |
| exposure | 0.7258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
