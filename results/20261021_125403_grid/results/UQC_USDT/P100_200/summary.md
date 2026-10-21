# EMA Hourly Continuation — UQC/USDT P100_200

**Symbol:** UQC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 176 |
| net_profit_factor | 0.2909 |
| net_win_rate | 0.2670 |
| gross_profit_factor | 0.4766 |
| gross_win_rate | 0.2898 |
| sharpe_ratio | -5.6640 |
| sortino_ratio | -1.0545 |
| max_drawdown | 0.7714 |
| cagr | -0.4430 |
| net_avg_win | 67.3216 |
| net_avg_loss | -84.3269 |
| avg_hold_time_bars | 48.7102 |
| exposure | 0.3880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
