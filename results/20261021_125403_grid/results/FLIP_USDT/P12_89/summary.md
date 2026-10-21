# EMA Hourly Continuation — FLIP/USDT P12_89

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.7088 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9535 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -2.3016 |
| sortino_ratio | -0.6640 |
| max_drawdown | 0.5794 |
| cagr | -0.2646 |
| net_avg_win | 65.7966 |
| net_avg_loss | -86.7216 |
| avg_hold_time_bars | 31.0898 |
| exposure | 0.5822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
