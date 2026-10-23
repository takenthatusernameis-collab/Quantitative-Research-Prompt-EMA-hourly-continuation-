# EMA Hourly Continuation — ILV/USDT P12_26

**Symbol:** ILV/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1362 |
| net_profit_factor | 0.3736 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.7913 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -10.6783 |
| sortino_ratio | -5.5809 |
| max_drawdown | 0.9991 |
| cagr | -0.9389 |
| net_avg_win | 10.2219 |
| net_avg_loss | -20.4755 |
| avg_hold_time_bars | 3.1204 |
| exposure | 0.1932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
