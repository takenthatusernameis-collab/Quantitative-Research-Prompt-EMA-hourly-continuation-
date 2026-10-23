# EMA Hourly Continuation — TRB/USDT P12_26

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1516 |
| net_profit_factor | 0.3977 |
| net_win_rate | 0.3793 |
| gross_profit_factor | 0.8761 |
| gross_win_rate | 0.4142 |
| sharpe_ratio | -13.5358 |
| sortino_ratio | -7.4497 |
| max_drawdown | 0.9999 |
| cagr | -0.9783 |
| net_avg_win | 11.4816 |
| net_avg_loss | -17.6422 |
| avg_hold_time_bars | 2.8252 |
| exposure | 0.1938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
