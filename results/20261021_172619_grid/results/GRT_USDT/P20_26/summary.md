# EMA Hourly Continuation — GRT/USDT P20_26

**Symbol:** GRT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.5008 |
| net_win_rate | 0.4076 |
| gross_profit_factor | 0.7075 |
| gross_win_rate | 0.4076 |
| sharpe_ratio | -3.0146 |
| sortino_ratio | -0.5817 |
| max_drawdown | 0.5156 |
| cagr | -0.2360 |
| net_avg_win | 65.9508 |
| net_avg_loss | -90.6067 |
| avg_hold_time_bars | 4.6848 |
| exposure | 0.0390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
