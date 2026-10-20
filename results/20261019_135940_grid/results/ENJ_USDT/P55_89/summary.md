# EMA Hourly Continuation — ENJ/USDT P55_89

**Symbol:** ENJ/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.5611 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 1.0081 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -5.2179 |
| sortino_ratio | -1.9004 |
| max_drawdown | 0.9002 |
| cagr | -0.5989 |
| net_avg_win | 36.9583 |
| net_avg_loss | -59.5517 |
| avg_hold_time_bars | 4.3008 |
| exposure | 0.1280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
