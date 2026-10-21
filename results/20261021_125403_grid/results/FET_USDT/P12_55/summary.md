# EMA Hourly Continuation — FET/USDT P12_55

**Symbol:** FET/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.9027 |
| net_win_rate | 0.5214 |
| gross_profit_factor | 1.0952 |
| gross_win_rate | 0.5214 |
| sharpe_ratio | -0.8208 |
| sortino_ratio | -0.2859 |
| max_drawdown | 0.4118 |
| cagr | -0.1280 |
| net_avg_win | 88.5023 |
| net_avg_loss | -106.7967 |
| avg_hold_time_bars | 12.9897 |
| exposure | 0.3454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
