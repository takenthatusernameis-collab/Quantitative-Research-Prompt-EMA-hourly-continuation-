# EMA Hourly Continuation — ADA/USDT P21_89

**Symbol:** ADA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7903 |
| net_win_rate | 0.5083 |
| gross_profit_factor | 1.0202 |
| gross_win_rate | 0.5083 |
| sharpe_ratio | -1.5625 |
| sortino_ratio | -0.4920 |
| max_drawdown | 0.4644 |
| cagr | -0.2033 |
| net_avg_win | 66.9065 |
| net_avg_loss | -87.5148 |
| avg_hold_time_bars | 14.8174 |
| exposure | 0.3246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
