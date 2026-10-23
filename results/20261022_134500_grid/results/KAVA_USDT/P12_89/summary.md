# EMA Hourly Continuation — KAVA/USDT P12_89

**Symbol:** KAVA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 777 |
| net_profit_factor | 0.5909 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.9960 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -5.9035 |
| sortino_ratio | -2.3000 |
| max_drawdown | 0.9478 |
| cagr | -0.6804 |
| net_avg_win | 38.6955 |
| net_avg_loss | -54.2365 |
| avg_hold_time_bars | 16.2021 |
| exposure | 0.5722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
