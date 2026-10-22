# EMA Hourly Continuation — XMR/USDT P20_89

**Symbol:** XMR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1116 |
| net_profit_factor | 0.3703 |
| net_win_rate | 0.4211 |
| gross_profit_factor | 0.7505 |
| gross_win_rate | 0.4301 |
| sharpe_ratio | -9.1403 |
| sortino_ratio | -4.2785 |
| max_drawdown | 0.9954 |
| cagr | -0.8825 |
| net_avg_win | 12.4526 |
| net_avg_loss | -24.4682 |
| avg_hold_time_bars | 6.4176 |
| exposure | 0.3255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
