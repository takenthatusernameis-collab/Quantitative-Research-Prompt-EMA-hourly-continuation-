# EMA Hourly Continuation — SOL/USDT P12_34

**Symbol:** SOL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.7298 |
| net_win_rate | 0.5009 |
| gross_profit_factor | 1.0182 |
| gross_win_rate | 0.5009 |
| sharpe_ratio | -2.5543 |
| sortino_ratio | -0.8605 |
| max_drawdown | 0.6404 |
| cagr | -0.3262 |
| net_avg_win | 61.5674 |
| net_avg_loss | -84.6658 |
| avg_hold_time_bars | 6.6951 |
| exposure | 0.1677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
