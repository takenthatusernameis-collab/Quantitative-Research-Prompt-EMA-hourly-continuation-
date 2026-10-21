# EMA Hourly Continuation — RUNE/USDT P34_100

**Symbol:** RUNE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.8433 |
| net_win_rate | 0.5271 |
| gross_profit_factor | 1.0854 |
| gross_win_rate | 0.5271 |
| sharpe_ratio | -0.9188 |
| sortino_ratio | -0.2607 |
| max_drawdown | 0.3618 |
| cagr | -0.1144 |
| net_avg_win | 69.3931 |
| net_avg_loss | -91.7252 |
| avg_hold_time_bars | 15.7494 |
| exposure | 0.2770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
