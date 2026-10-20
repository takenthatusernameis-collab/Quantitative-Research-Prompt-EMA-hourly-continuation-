# EMA Hourly Continuation — GLM/USDT P12_50

**Symbol:** GLM/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 989 |
| net_profit_factor | 0.4512 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8117 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -6.8764 |
| sortino_ratio | -3.0470 |
| max_drawdown | 0.9761 |
| cagr | -0.7715 |
| net_avg_win | 18.0232 |
| net_avg_loss | -32.6744 |
| avg_hold_time_bars | 8.7321 |
| exposure | 0.3925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
