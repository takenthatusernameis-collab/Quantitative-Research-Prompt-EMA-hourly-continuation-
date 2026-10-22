# EMA Hourly Continuation — SUN/USDT P21_55

**Symbol:** SUN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 806 |
| net_profit_factor | 0.3150 |
| net_win_rate | 0.3610 |
| gross_profit_factor | 0.8167 |
| gross_win_rate | 0.4231 |
| sharpe_ratio | -11.1133 |
| sortino_ratio | -4.5313 |
| max_drawdown | 0.9976 |
| cagr | -0.9093 |
| net_avg_win | 15.7649 |
| net_avg_loss | -28.2798 |
| avg_hold_time_bars | 7.6538 |
| exposure | 0.2792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
