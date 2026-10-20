# EMA Hourly Continuation — UQC/USDT P50_55

**Symbol:** UQC/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.0506 |
| net_win_rate | 0.1575 |
| gross_profit_factor | 0.1968 |
| gross_win_rate | 0.2101 |
| sharpe_ratio | -13.4458 |
| sortino_ratio | -4.6847 |
| max_drawdown | 0.9987 |
| cagr | -0.9289 |
| net_avg_win | 7.3862 |
| net_avg_loss | -27.3224 |
| avg_hold_time_bars | 9.8534 |
| exposure | 0.2038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
