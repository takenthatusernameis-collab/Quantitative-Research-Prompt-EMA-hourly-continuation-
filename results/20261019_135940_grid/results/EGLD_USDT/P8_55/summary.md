# EMA Hourly Continuation — EGLD/USDT P8_55

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.6109 |
| net_win_rate | 0.4836 |
| gross_profit_factor | 1.0374 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -5.3389 |
| sortino_ratio | -2.3739 |
| max_drawdown | 0.9472 |
| cagr | -0.6847 |
| net_avg_win | 30.5287 |
| net_avg_loss | -46.7936 |
| avg_hold_time_bars | 10.6935 |
| exposure | 0.4885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
