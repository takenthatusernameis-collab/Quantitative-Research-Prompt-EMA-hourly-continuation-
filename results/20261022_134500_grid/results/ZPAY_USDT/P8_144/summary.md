# EMA Hourly Continuation — ZPAY/USDT P8_144

**Symbol:** ZPAY/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.5170 |
| net_win_rate | 0.3614 |
| gross_profit_factor | 0.6242 |
| gross_win_rate | 0.3614 |
| sharpe_ratio | -4.4917 |
| sortino_ratio | -1.2556 |
| max_drawdown | 0.7799 |
| cagr | -0.4434 |
| net_avg_win | 56.5891 |
| net_avg_loss | -61.9436 |
| avg_hold_time_bars | 37.8317 |
| exposure | 0.6916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
