# EMA Hourly Continuation — QI/USDT P26_55

**Symbol:** QI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 846 |
| net_profit_factor | 0.5289 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9790 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -5.8610 |
| sortino_ratio | -2.4018 |
| max_drawdown | 0.9505 |
| cagr | -0.6872 |
| net_avg_win | 26.2415 |
| net_avg_loss | -45.5659 |
| avg_hold_time_bars | 4.8156 |
| exposure | 0.1844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
