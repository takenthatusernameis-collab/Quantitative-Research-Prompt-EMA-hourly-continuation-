# EMA Hourly Continuation — BAT/USDT P21_200

**Symbol:** BAT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.6272 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9325 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -2.7380 |
| sortino_ratio | -0.7819 |
| max_drawdown | 0.6530 |
| cagr | -0.3094 |
| net_avg_win | 51.6892 |
| net_avg_loss | -76.2221 |
| avg_hold_time_bars | 32.4902 |
| exposure | 0.6055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
