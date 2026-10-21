# EMA Hourly Continuation — RLC/USDT P12_20

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6418 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 0.9603 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -2.9490 |
| sortino_ratio | -0.8977 |
| max_drawdown | 0.6651 |
| cagr | -0.3353 |
| net_avg_win | 51.9955 |
| net_avg_loss | -78.8796 |
| avg_hold_time_bars | 4.8683 |
| exposure | 0.0991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
