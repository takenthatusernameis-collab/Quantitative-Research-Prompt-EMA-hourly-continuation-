# EMA Hourly Continuation — HNT/USDT P55_89

**Symbol:** HNT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.6872 |
| net_win_rate | 0.4785 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -1.9503 |
| sortino_ratio | -0.5031 |
| max_drawdown | 0.4716 |
| cagr | -0.2061 |
| net_avg_win | 61.9313 |
| net_avg_loss | -82.7035 |
| avg_hold_time_bars | 7.6595 |
| exposure | 0.1135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
