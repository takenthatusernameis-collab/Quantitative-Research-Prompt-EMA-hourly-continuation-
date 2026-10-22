# EMA Hourly Continuation — XEC/USDT P20_26

**Symbol:** XEC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1300 |
| net_profit_factor | 0.2370 |
| net_win_rate | 0.3592 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4323 |
| sharpe_ratio | -15.4009 |
| sortino_ratio | -8.1286 |
| max_drawdown | 1.0000 |
| cagr | -0.9869 |
| net_avg_win | 6.6498 |
| net_avg_loss | -15.7326 |
| avg_hold_time_bars | 2.4577 |
| exposure | 0.1446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
