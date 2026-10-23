# EMA Hourly Continuation — SSV/USDT P21_26

**Symbol:** SSV/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1272 |
| net_profit_factor | 0.2901 |
| net_win_rate | 0.3836 |
| gross_profit_factor | 0.7275 |
| gross_win_rate | 0.4151 |
| sharpe_ratio | -13.6102 |
| sortino_ratio | -6.9565 |
| max_drawdown | 0.9999 |
| cagr | -0.9746 |
| net_avg_win | 8.3713 |
| net_avg_loss | -17.9646 |
| avg_hold_time_bars | 2.0943 |
| exposure | 0.1205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
