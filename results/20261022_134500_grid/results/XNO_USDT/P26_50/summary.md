# EMA Hourly Continuation — XNO/USDT P26_50

**Symbol:** XNO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1139 |
| net_profit_factor | 0.4040 |
| net_win_rate | 0.3793 |
| gross_profit_factor | 0.7948 |
| gross_win_rate | 0.3960 |
| sharpe_ratio | -11.2269 |
| sortino_ratio | -5.3783 |
| max_drawdown | 0.9989 |
| cagr | -0.9329 |
| net_avg_win | 15.6731 |
| net_avg_loss | -23.7050 |
| avg_hold_time_bars | 3.2687 |
| exposure | 0.1692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
