# EMA Hourly Continuation — ATH/USDT P12_100

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.8921 |
| net_win_rate | 0.5178 |
| gross_profit_factor | 1.0567 |
| gross_win_rate | 0.5178 |
| sharpe_ratio | -0.7125 |
| sortino_ratio | -0.2242 |
| max_drawdown | 0.2911 |
| cagr | -0.1024 |
| net_avg_win | 79.7148 |
| net_avg_loss | -95.9486 |
| avg_hold_time_bars | 24.4867 |
| exposure | 0.5341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
