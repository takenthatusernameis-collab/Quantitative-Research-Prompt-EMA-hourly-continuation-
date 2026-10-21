# EMA Hourly Continuation — SUI/USDT P34_50

**Symbol:** SUI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.9716 |
| net_win_rate | 0.5721 |
| gross_profit_factor | 1.3230 |
| gross_win_rate | 0.5721 |
| sharpe_ratio | -0.0919 |
| sortino_ratio | -0.0200 |
| max_drawdown | 0.1775 |
| cagr | -0.0129 |
| net_avg_win | 86.2206 |
| net_avg_loss | -118.6353 |
| avg_hold_time_bars | 5.3018 |
| exposure | 0.0535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
