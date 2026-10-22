# EMA Hourly Continuation — APE/USDT P21_55

**Symbol:** APE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 986 |
| net_profit_factor | 0.5136 |
| net_win_rate | 0.4696 |
| gross_profit_factor | 0.8919 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -6.3026 |
| sortino_ratio | -2.7839 |
| max_drawdown | 0.9678 |
| cagr | -0.7411 |
| net_avg_win | 22.0415 |
| net_avg_loss | -37.9911 |
| avg_hold_time_bars | 4.5680 |
| exposure | 0.2047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
