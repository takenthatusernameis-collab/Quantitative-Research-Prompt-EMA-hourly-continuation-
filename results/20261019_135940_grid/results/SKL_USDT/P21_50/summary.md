# EMA Hourly Continuation — SKL/USDT P21_50

**Symbol:** SKL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1035 |
| net_profit_factor | 0.5057 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8882 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -6.9971 |
| sortino_ratio | -3.1889 |
| max_drawdown | 0.9794 |
| cagr | -0.7827 |
| net_avg_win | 21.0726 |
| net_avg_loss | -35.3451 |
| avg_hold_time_bars | 4.5990 |
| exposure | 0.2164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
