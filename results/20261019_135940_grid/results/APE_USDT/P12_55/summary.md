# EMA Hourly Continuation — APE/USDT P12_55

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1028 |
| net_profit_factor | 0.5860 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.9523 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -6.2176 |
| sortino_ratio | -2.8065 |
| max_drawdown | 0.9681 |
| cagr | -0.7394 |
| net_avg_win | 28.8445 |
| net_avg_loss | -42.1132 |
| avg_hold_time_bars | 8.1556 |
| exposure | 0.3811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
