# EMA Hourly Continuation — ZPAY/USDT P20_144

**Symbol:** ZPAY/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.4989 |
| net_win_rate | 0.3714 |
| gross_profit_factor | 0.6091 |
| gross_win_rate | 0.3714 |
| sharpe_ratio | -4.3229 |
| sortino_ratio | -1.1749 |
| max_drawdown | 0.7563 |
| cagr | -0.4281 |
| net_avg_win | 52.6263 |
| net_avg_loss | -62.3259 |
| avg_hold_time_bars | 36.6494 |
| exposure | 0.6385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
