# EMA Hourly Continuation — UMA/USDT P12_89

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.6039 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9331 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -4.0351 |
| sortino_ratio | -1.5032 |
| max_drawdown | 0.8484 |
| cagr | -0.5163 |
| net_avg_win | 37.6001 |
| net_avg_loss | -57.2171 |
| avg_hold_time_bars | 15.8028 |
| exposure | 0.5100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
