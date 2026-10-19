# EMA Hourly Continuation — UNI/USDT P12_89

**Symbol:** UNI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.6083 |
| net_win_rate | 0.4720 |
| gross_profit_factor | 0.9308 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -4.3905 |
| sortino_ratio | -1.6630 |
| max_drawdown | 0.8702 |
| cagr | -0.5513 |
| net_avg_win | 39.0023 |
| net_avg_loss | -57.3044 |
| avg_hold_time_bars | 15.6908 |
| exposure | 0.5214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
