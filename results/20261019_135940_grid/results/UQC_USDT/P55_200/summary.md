# EMA Hourly Continuation — UQC/USDT P55_200

**Symbol:** UQC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.2724 |
| net_win_rate | 0.3099 |
| gross_profit_factor | 0.4507 |
| gross_win_rate | 0.3140 |
| sharpe_ratio | -5.6074 |
| sortino_ratio | -1.2204 |
| max_drawdown | 0.7899 |
| cagr | -0.4613 |
| net_avg_win | 39.4284 |
| net_avg_loss | -65.0093 |
| avg_hold_time_bars | 52.2149 |
| exposure | 0.5719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
