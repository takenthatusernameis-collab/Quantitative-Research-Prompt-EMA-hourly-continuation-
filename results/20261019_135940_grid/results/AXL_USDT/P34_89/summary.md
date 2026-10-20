# EMA Hourly Continuation — AXL/USDT P34_89

**Symbol:** AXL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 772 |
| net_profit_factor | 0.5826 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.8885 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -5.5954 |
| sortino_ratio | -2.1848 |
| max_drawdown | 0.9298 |
| cagr | -0.6485 |
| net_avg_win | 37.9976 |
| net_avg_loss | -51.6053 |
| avg_hold_time_bars | 7.1075 |
| exposure | 0.2483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
