# EMA Hourly Continuation — ACE/USDT P8_12

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6837 |
| net_win_rate | 0.5067 |
| gross_profit_factor | 1.0419 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -2.5549 |
| sortino_ratio | -0.7741 |
| max_drawdown | 0.5930 |
| cagr | -0.2998 |
| net_avg_win | 56.4606 |
| net_avg_loss | -84.8247 |
| avg_hold_time_bars | 6.5424 |
| exposure | 0.1326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
