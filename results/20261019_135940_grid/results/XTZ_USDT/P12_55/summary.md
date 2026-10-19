# EMA Hourly Continuation — XTZ/USDT P12_55

**Symbol:** XTZ/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1008 |
| net_profit_factor | 0.4800 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.9342 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -6.8975 |
| sortino_ratio | -3.0820 |
| max_drawdown | 0.9773 |
| cagr | -0.7778 |
| net_avg_win | 19.3942 |
| net_avg_loss | -34.6029 |
| avg_hold_time_bars | 8.3472 |
| exposure | 0.3825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
