# EMA Hourly Continuation — LISTA/USDT P12_55

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 838 |
| net_profit_factor | 0.6535 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.9536 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -4.5767 |
| sortino_ratio | -1.9393 |
| max_drawdown | 0.8853 |
| cagr | -0.5996 |
| net_avg_win | 42.4251 |
| net_avg_loss | -57.0637 |
| avg_hold_time_bars | 9.7136 |
| exposure | 0.3980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
