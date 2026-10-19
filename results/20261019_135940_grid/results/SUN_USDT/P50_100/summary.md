# EMA Hourly Continuation — SUN/USDT P50_100

**Symbol:** SUN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.2684 |
| net_win_rate | 0.3504 |
| gross_profit_factor | 0.6699 |
| gross_win_rate | 0.4085 |
| sharpe_ratio | -9.4198 |
| sortino_ratio | -3.2107 |
| max_drawdown | 0.9873 |
| cagr | -0.8224 |
| net_avg_win | 18.2028 |
| net_avg_loss | -36.5707 |
| avg_hold_time_bars | 7.6761 |
| exposure | 0.1973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
