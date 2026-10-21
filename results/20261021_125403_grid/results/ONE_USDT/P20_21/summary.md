# EMA Hourly Continuation — ONE/USDT P20_21

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 128 |
| net_profit_factor | 0.9129 |
| net_win_rate | 0.5547 |
| gross_profit_factor | 1.2370 |
| gross_win_rate | 0.5547 |
| sharpe_ratio | -0.2926 |
| sortino_ratio | -0.0481 |
| max_drawdown | 0.1400 |
| cagr | -0.0232 |
| net_avg_win | 84.4630 |
| net_avg_loss | -115.2431 |
| avg_hold_time_bars | 4.2422 |
| exposure | 0.0247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
