# EMA Hourly Continuation — MANA/USDT P12_144

**Symbol:** MANA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.5924 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9431 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -3.1618 |
| sortino_ratio | -0.8607 |
| max_drawdown | 0.6699 |
| cagr | -0.3482 |
| net_avg_win | 52.3041 |
| net_avg_loss | -80.7913 |
| avg_hold_time_bars | 42.4595 |
| exposure | 0.7392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
