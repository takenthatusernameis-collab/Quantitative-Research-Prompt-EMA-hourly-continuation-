# EMA Hourly Continuation — UQC/USDT P34_200

**Symbol:** UQC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.3191 |
| net_win_rate | 0.3037 |
| gross_profit_factor | 0.4337 |
| gross_win_rate | 0.3037 |
| sharpe_ratio | -4.8861 |
| sortino_ratio | -1.0001 |
| max_drawdown | 0.7012 |
| cagr | -0.3805 |
| net_avg_win | 50.5531 |
| net_avg_loss | -69.1113 |
| avg_hold_time_bars | 68.6869 |
| exposure | 0.6653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
