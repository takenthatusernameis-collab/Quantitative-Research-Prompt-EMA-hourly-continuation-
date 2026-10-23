# EMA Hourly Continuation — BOSON/USDT P8_89

**Symbol:** BOSON/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 783 |
| net_profit_factor | 0.6972 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.9421 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -4.1731 |
| sortino_ratio | -1.6351 |
| max_drawdown | 0.8589 |
| cagr | -0.5392 |
| net_avg_win | 55.7513 |
| net_avg_loss | -65.9842 |
| avg_hold_time_bars | 16.3499 |
| exposure | 0.5819 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
