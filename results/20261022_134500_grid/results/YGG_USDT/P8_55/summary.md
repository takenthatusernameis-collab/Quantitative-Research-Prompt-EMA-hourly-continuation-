# EMA Hourly Continuation — YGG/USDT P8_55

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1029 |
| net_profit_factor | 0.6952 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 1.0017 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -4.6280 |
| sortino_ratio | -2.0861 |
| max_drawdown | 0.9201 |
| cagr | -0.6290 |
| net_avg_win | 42.3028 |
| net_avg_loss | -56.4047 |
| avg_hold_time_bars | 10.5053 |
| exposure | 0.4892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
