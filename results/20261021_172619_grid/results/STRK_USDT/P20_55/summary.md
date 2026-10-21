# EMA Hourly Continuation — STRK/USDT P20_55

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7762 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9884 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.7653 |
| sortino_ratio | -0.5623 |
| max_drawdown | 0.4862 |
| cagr | -0.2278 |
| net_avg_win | 67.3340 |
| net_avg_loss | -86.0467 |
| avg_hold_time_bars | 8.3988 |
| exposure | 0.1886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
