# EMA Hourly Continuation — TNSR/USDT P26_89

**Symbol:** TNSR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.8343 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0469 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -1.2715 |
| sortino_ratio | -0.4167 |
| max_drawdown | 0.4350 |
| cagr | -0.1767 |
| net_avg_win | 72.5687 |
| net_avg_loss | -92.1147 |
| avg_hold_time_bars | 12.5029 |
| exposure | 0.2959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
