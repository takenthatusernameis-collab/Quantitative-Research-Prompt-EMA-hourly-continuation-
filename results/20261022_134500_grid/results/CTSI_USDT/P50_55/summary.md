# EMA Hourly Continuation — CTSI/USDT P50_55

**Symbol:** CTSI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 816 |
| net_profit_factor | 0.2800 |
| net_win_rate | 0.3897 |
| gross_profit_factor | 0.8614 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -10.6720 |
| sortino_ratio | -4.4213 |
| max_drawdown | 0.9969 |
| cagr | -0.8996 |
| net_avg_win | 12.1930 |
| net_avg_loss | -27.8038 |
| avg_hold_time_bars | 2.9730 |
| exposure | 0.1103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
