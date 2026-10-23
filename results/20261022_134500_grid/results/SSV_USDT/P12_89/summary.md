# EMA Hourly Continuation — SSV/USDT P12_89

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 758 |
| net_profit_factor | 0.5943 |
| net_win_rate | 0.4406 |
| gross_profit_factor | 0.8566 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -5.0994 |
| sortino_ratio | -1.9689 |
| max_drawdown | 0.9187 |
| cagr | -0.6093 |
| net_avg_win | 39.7689 |
| net_avg_loss | -52.7094 |
| avg_hold_time_bars | 16.1187 |
| exposure | 0.5529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
