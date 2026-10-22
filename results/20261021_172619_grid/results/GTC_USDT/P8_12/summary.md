# EMA Hourly Continuation — GTC/USDT P8_12

**Symbol:** GTC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.5905 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -3.6633 |
| sortino_ratio | -1.0871 |
| max_drawdown | 0.7168 |
| cagr | -0.3935 |
| net_avg_win | 52.6229 |
| net_avg_loss | -74.6394 |
| avg_hold_time_bars | 4.8070 |
| exposure | 0.0940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
