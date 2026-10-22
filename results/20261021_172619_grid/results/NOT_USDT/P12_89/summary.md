# EMA Hourly Continuation — NOT/USDT P12_89

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.8699 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0447 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -0.8727 |
| sortino_ratio | -0.2662 |
| max_drawdown | 0.2953 |
| cagr | -0.1183 |
| net_avg_win | 78.6393 |
| net_avg_loss | -95.5219 |
| avg_hold_time_bars | 25.8073 |
| exposure | 0.5286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
