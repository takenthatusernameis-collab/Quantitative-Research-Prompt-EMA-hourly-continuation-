# EMA Hourly Continuation — SSV/USDT P8_34

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1354 |
| net_profit_factor | 0.5739 |
| net_win_rate | 0.4357 |
| gross_profit_factor | 0.8956 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -8.2757 |
| sortino_ratio | -4.2673 |
| max_drawdown | 0.9947 |
| cagr | -0.8745 |
| net_avg_win | 22.7079 |
| net_avg_loss | -30.5555 |
| avg_hold_time_bars | 6.4638 |
| exposure | 0.3960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
