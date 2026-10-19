# EMA Hourly Continuation — WIF/USDT P12_20

**Symbol:** WIF/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1481 |
| net_profit_factor | 0.4837 |
| net_win_rate | 0.4308 |
| gross_profit_factor | 0.9306 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -11.3971 |
| sortino_ratio | -6.1732 |
| max_drawdown | 0.9997 |
| cagr | -0.9581 |
| net_avg_win | 14.6810 |
| net_avg_loss | -22.9692 |
| avg_hold_time_bars | 2.0108 |
| exposure | 0.1354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
