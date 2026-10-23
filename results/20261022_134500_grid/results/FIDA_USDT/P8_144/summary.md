# EMA Hourly Continuation — FIDA/USDT P8_144

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.5766 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.8285 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -3.6857 |
| sortino_ratio | -1.1834 |
| max_drawdown | 0.7632 |
| cagr | -0.4312 |
| net_avg_win | 43.4274 |
| net_avg_loss | -62.6786 |
| avg_hold_time_bars | 31.1546 |
| exposure | 0.7387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
