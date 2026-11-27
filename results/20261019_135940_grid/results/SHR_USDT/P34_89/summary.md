# EMA Hourly Continuation — SHR/USDT P34_89

**Symbol:** SHR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 935 |
| net_profit_factor | 0.3840 |
| net_win_rate | 0.3412 |
| gross_profit_factor | 0.5608 |
| gross_win_rate | 0.3433 |
| sharpe_ratio | -9.2174 |
| sortino_ratio | -3.9239 |
| max_drawdown | 0.9922 |
| cagr | -0.8533 |
| net_avg_win | 19.3882 |
| net_avg_loss | -26.1460 |
| avg_hold_time_bars | 5.6567 |
| exposure | 0.2393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
