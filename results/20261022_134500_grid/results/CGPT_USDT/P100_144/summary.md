# EMA Hourly Continuation — CGPT/USDT P100_144

**Symbol:** CGPT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.4757 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.8749 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -4.6872 |
| sortino_ratio | -1.3984 |
| max_drawdown | 0.8280 |
| cagr | -0.4997 |
| net_avg_win | 36.2989 |
| net_avg_loss | -64.1657 |
| avg_hold_time_bars | 3.4945 |
| exposure | 0.0716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
