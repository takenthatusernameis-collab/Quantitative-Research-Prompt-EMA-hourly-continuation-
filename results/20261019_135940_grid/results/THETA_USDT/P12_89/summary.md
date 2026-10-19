# EMA Hourly Continuation — THETA/USDT P12_89

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.6209 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4709 |
| sharpe_ratio | -4.0836 |
| sortino_ratio | -1.4875 |
| max_drawdown | 0.8423 |
| cagr | -0.5075 |
| net_avg_win | 43.6361 |
| net_avg_loss | -61.0742 |
| avg_hold_time_bars | 18.6110 |
| exposure | 0.5676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
