# EMA Hourly Continuation — XMR/USDT P21_89

**Symbol:** XMR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1123 |
| net_profit_factor | 0.3782 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.7872 |
| gross_win_rate | 0.4301 |
| sharpe_ratio | -9.2859 |
| sortino_ratio | -4.3565 |
| max_drawdown | 0.9960 |
| cagr | -0.8884 |
| net_avg_win | 12.8055 |
| net_avg_loss | -24.6407 |
| avg_hold_time_bars | 6.1256 |
| exposure | 0.3127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
