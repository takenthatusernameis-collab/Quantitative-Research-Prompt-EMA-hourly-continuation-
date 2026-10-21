# EMA Hourly Continuation — IOTX/USDT P20_55

**Symbol:** IOTX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.7715 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0514 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -2.0300 |
| sortino_ratio | -0.6872 |
| max_drawdown | 0.5877 |
| cagr | -0.2701 |
| net_avg_win | 64.9615 |
| net_avg_loss | -88.5721 |
| avg_hold_time_bars | 7.6227 |
| exposure | 0.1920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
