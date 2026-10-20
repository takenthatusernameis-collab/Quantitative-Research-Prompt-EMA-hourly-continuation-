# EMA Hourly Continuation — CTSI/USDT P55_200

**Symbol:** CTSI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.6846 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9478 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -2.7093 |
| sortino_ratio | -0.8077 |
| max_drawdown | 0.6329 |
| cagr | -0.3113 |
| net_avg_win | 63.1400 |
| net_avg_loss | -84.1794 |
| avg_hold_time_bars | 18.2808 |
| exposure | 0.3640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
