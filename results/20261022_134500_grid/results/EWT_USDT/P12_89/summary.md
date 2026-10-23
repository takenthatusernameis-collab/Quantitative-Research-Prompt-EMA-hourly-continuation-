# EMA Hourly Continuation — EWT/USDT P12_89

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 795 |
| net_profit_factor | 0.4718 |
| net_win_rate | 0.4151 |
| gross_profit_factor | 0.7350 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -6.5150 |
| sortino_ratio | -2.5687 |
| max_drawdown | 0.9607 |
| cagr | -0.7155 |
| net_avg_win | 25.9101 |
| net_avg_loss | -38.9778 |
| avg_hold_time_bars | 11.3057 |
| exposure | 0.4085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
