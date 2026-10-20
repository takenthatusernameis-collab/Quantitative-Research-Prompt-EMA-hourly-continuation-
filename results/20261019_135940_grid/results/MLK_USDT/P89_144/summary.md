# EMA Hourly Continuation — MLK/USDT P89_144

**Symbol:** MLK/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.2466 |
| net_win_rate | 0.2783 |
| gross_profit_factor | 0.4893 |
| gross_win_rate | 0.2841 |
| sharpe_ratio | -11.7938 |
| sortino_ratio | -4.5220 |
| max_drawdown | 0.9970 |
| cagr | -0.8990 |
| net_avg_win | 16.8242 |
| net_avg_loss | -26.3083 |
| avg_hold_time_bars | 4.2984 |
| exposure | 0.1356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
