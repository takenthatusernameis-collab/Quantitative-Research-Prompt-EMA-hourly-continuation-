# EMA Hourly Continuation — ONT/USDT P89_100

**Symbol:** ONT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 136 |
| net_profit_factor | 0.5213 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.8311 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -2.3208 |
| sortino_ratio | -0.3882 |
| max_drawdown | 0.3870 |
| cagr | -0.1638 |
| net_avg_win | 63.7951 |
| net_avg_loss | -102.5260 |
| avg_hold_time_bars | 5.3676 |
| exposure | 0.0330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
