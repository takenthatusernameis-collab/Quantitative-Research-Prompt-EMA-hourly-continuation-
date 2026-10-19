# EMA Hourly Continuation — AXS/USDT P20_50

**Symbol:** AXS/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 915 |
| net_profit_factor | 0.5379 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.9917 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -6.2071 |
| sortino_ratio | -2.6419 |
| max_drawdown | 0.9624 |
| cagr | -0.7238 |
| net_avg_win | 25.8924 |
| net_avg_loss | -43.0561 |
| avg_hold_time_bars | 5.0689 |
| exposure | 0.2099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
