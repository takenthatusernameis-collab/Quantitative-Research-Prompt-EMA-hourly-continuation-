# EMA Hourly Continuation — RLC/USDT P12_20

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1394 |
| net_profit_factor | 0.3911 |
| net_win_rate | 0.4333 |
| gross_profit_factor | 0.9488 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -11.4592 |
| sortino_ratio | -6.0850 |
| max_drawdown | 0.9996 |
| cagr | -0.9535 |
| net_avg_win | 10.6312 |
| net_avg_loss | -20.7807 |
| avg_hold_time_bars | 2.6908 |
| exposure | 0.1705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
