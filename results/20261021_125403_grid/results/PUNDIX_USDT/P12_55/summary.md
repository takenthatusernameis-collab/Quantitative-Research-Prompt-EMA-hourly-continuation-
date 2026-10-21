# EMA Hourly Continuation — PUNDIX/USDT P12_55

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.7025 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9624 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -3.2825 |
| sortino_ratio | -1.2251 |
| max_drawdown | 0.7688 |
| cagr | -0.4295 |
| net_avg_win | 54.0695 |
| net_avg_loss | -72.1586 |
| avg_hold_time_bars | 11.9868 |
| exposure | 0.3716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
