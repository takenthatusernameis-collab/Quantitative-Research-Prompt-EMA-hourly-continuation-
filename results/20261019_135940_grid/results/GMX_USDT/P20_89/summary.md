# EMA Hourly Continuation — GMX/USDT P20_89

**Symbol:** GMX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 763 |
| net_profit_factor | 0.5667 |
| net_win_rate | 0.4456 |
| gross_profit_factor | 0.9145 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -5.5038 |
| sortino_ratio | -2.1316 |
| max_drawdown | 0.9265 |
| cagr | -0.6420 |
| net_avg_win | 35.5528 |
| net_avg_loss | -50.4252 |
| avg_hold_time_bars | 10.8768 |
| exposure | 0.3772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
