# EMA Hourly Continuation — INJ/USDT P89_144

**Symbol:** INJ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.6676 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.8460 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -2.0342 |
| sortino_ratio | -0.4641 |
| max_drawdown | 0.4349 |
| cagr | -0.1920 |
| net_avg_win | 70.5834 |
| net_avg_loss | -89.7490 |
| avg_hold_time_bars | 7.3191 |
| exposure | 0.0855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
