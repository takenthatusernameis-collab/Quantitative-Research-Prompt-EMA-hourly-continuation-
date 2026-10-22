# EMA Hourly Continuation — UNI/USDT P12_20

**Symbol:** UNI/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1492 |
| net_profit_factor | 0.3020 |
| net_win_rate | 0.3760 |
| gross_profit_factor | 0.7802 |
| gross_win_rate | 0.4042 |
| sharpe_ratio | -14.7328 |
| sortino_ratio | -8.1659 |
| max_drawdown | 1.0000 |
| cagr | -0.9857 |
| net_avg_win | 7.7116 |
| net_avg_loss | -15.3877 |
| avg_hold_time_bars | 1.9598 |
| exposure | 0.1329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
