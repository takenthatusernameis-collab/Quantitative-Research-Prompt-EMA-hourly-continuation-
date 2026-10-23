# EMA Hourly Continuation — ERG/USDT P12_144

**Symbol:** ERG/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.4743 |
| net_win_rate | 0.4253 |
| gross_profit_factor | 0.7073 |
| gross_win_rate | 0.4329 |
| sharpe_ratio | -5.2758 |
| sortino_ratio | -1.9141 |
| max_drawdown | 0.9019 |
| cagr | -0.5993 |
| net_avg_win | 28.7760 |
| net_avg_loss | -44.9051 |
| avg_hold_time_bars | 18.8220 |
| exposure | 0.5672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
