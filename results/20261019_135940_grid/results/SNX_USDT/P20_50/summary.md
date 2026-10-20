# EMA Hourly Continuation — SNX/USDT P20_50

**Symbol:** SNX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1015 |
| net_profit_factor | 0.5493 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 1.0061 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -6.2678 |
| sortino_ratio | -2.8001 |
| max_drawdown | 0.9690 |
| cagr | -0.7446 |
| net_avg_win | 24.3272 |
| net_avg_loss | -40.5262 |
| avg_hold_time_bars | 4.5488 |
| exposure | 0.2089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
