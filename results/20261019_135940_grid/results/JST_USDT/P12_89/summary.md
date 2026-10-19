# EMA Hourly Continuation — JST/USDT P12_89

**Symbol:** JST/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.4318 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 0.9420 |
| gross_win_rate | 0.5009 |
| sharpe_ratio | -4.8129 |
| sortino_ratio | -1.5599 |
| max_drawdown | 0.8761 |
| cagr | -0.5471 |
| net_avg_win | 25.2644 |
| net_avg_loss | -53.0070 |
| avg_hold_time_bars | 24.0932 |
| exposure | 0.5964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
