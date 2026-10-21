# EMA Hourly Continuation — GRT/USDT P12_20

**Symbol:** GRT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.6663 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9398 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -2.3920 |
| sortino_ratio | -0.5845 |
| max_drawdown | 0.5119 |
| cagr | -0.2350 |
| net_avg_win | 70.5742 |
| net_avg_loss | -96.2211 |
| avg_hold_time_bars | 5.0411 |
| exposure | 0.0666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
