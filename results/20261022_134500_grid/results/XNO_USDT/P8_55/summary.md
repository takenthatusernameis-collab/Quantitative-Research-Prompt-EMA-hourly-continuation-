# EMA Hourly Continuation — XNO/USDT P8_55

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1311 |
| net_profit_factor | 0.4810 |
| net_win_rate | 0.3905 |
| gross_profit_factor | 0.7661 |
| gross_win_rate | 0.4027 |
| sharpe_ratio | -10.0178 |
| sortino_ratio | -5.0907 |
| max_drawdown | 0.9982 |
| cagr | -0.9182 |
| net_avg_win | 18.0673 |
| net_avg_loss | -24.0699 |
| avg_hold_time_bars | 7.2471 |
| exposure | 0.4319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
