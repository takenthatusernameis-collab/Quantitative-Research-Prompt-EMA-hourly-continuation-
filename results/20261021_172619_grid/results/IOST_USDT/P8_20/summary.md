# EMA Hourly Continuation — IOST/USDT P8_20

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 749 |
| net_profit_factor | 0.6843 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0812 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -3.6502 |
| sortino_ratio | -1.4395 |
| max_drawdown | 0.8129 |
| cagr | -0.4820 |
| net_avg_win | 45.9871 |
| net_avg_loss | -69.5768 |
| avg_hold_time_bars | 5.3178 |
| exposure | 0.1810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
