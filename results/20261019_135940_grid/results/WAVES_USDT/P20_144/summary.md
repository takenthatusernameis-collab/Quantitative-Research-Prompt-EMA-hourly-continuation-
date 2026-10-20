# EMA Hourly Continuation — WAVES/USDT P20_144

**Symbol:** WAVES/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.5426 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8848 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -4.9000 |
| sortino_ratio | -1.7203 |
| max_drawdown | 0.8880 |
| cagr | -0.5716 |
| net_avg_win | 36.4211 |
| net_avg_loss | -55.9971 |
| avg_hold_time_bars | 18.3946 |
| exposure | 0.5276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
