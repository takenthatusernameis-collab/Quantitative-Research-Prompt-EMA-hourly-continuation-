# EMA Hourly Continuation — COMP/USDT P20_144

**Symbol:** COMP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.6393 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 1.0078 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -3.0925 |
| sortino_ratio | -1.0011 |
| max_drawdown | 0.7131 |
| cagr | -0.3798 |
| net_avg_win | 47.6227 |
| net_avg_loss | -72.0020 |
| avg_hold_time_bars | 23.6106 |
| exposure | 0.5677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
