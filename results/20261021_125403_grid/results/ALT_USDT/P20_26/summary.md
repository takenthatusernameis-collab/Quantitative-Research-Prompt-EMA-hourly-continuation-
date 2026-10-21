# EMA Hourly Continuation — ALT/USDT P20_26

**Symbol:** ALT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.5922 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.8494 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -3.1015 |
| sortino_ratio | -0.8609 |
| max_drawdown | 0.6406 |
| cagr | -0.3269 |
| net_avg_win | 52.2755 |
| net_avg_loss | -76.4735 |
| avg_hold_time_bars | 5.4377 |
| exposure | 0.0932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
