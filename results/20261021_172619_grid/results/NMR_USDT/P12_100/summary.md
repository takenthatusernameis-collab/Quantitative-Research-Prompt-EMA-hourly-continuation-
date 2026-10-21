# EMA Hourly Continuation — NMR/USDT P12_100

**Symbol:** NMR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.7819 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9731 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -2.0419 |
| sortino_ratio | -0.6872 |
| max_drawdown | 0.5859 |
| cagr | -0.2722 |
| net_avg_win | 72.1718 |
| net_avg_loss | -88.7311 |
| avg_hold_time_bars | 20.8402 |
| exposure | 0.5276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
